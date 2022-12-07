const express = require("express");
const multer = require("multer");
const upload = multer({ dest: "uploads/" });
var fs = require("fs");
var Buffer = require("buffer").Buffer;

const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(express.static("public"));

app.post("/upload_files", upload.array("files"), uploadFiles);

const ALLOWED_FILES_TYPES = ["ffd8ffe0", "ffd8ffe1", "89504e47", "47494638"];

async function uploadFiles(req, res) {
  console.log(req.files);

  if (req.files.length === 0)
    return res.json({ message: "You should upload a file !", type: "error" });

  if (req.files.length > 1)
    return res.json({
      message: "YOu should upload only one file",
      type: "error",
    });

  if (
    !req.files[0].originalname.endsWith(".jpg") &&
    !req.files[0].originalname.endsWith(".png")
  )
    return res.json({
      message: "Make sure you uploaded a picture in a .png/.jpg format",
      type: "error",
    });

  let FLAG = false;
  fs.open(req.files[0].path, "r", function (status, fd) {
    if (status) {
      return;
    }
    var buffer = new Buffer(30);
    fs.read(fd, buffer, 0, 30, 0, async function () {
      const magicNumber = buffer.toString("hex", 0, 4);
      if (!ALLOWED_FILES_TYPES.includes(magicNumber)) {
        FLAG = true;
        // deleting file , after we have done the check so my storage doesn't get depleted ( not task related )
        fs.unlink(req.files[0].path, () => {
          console.log("done, deleting file");
        });
        return FLAG
          ? res.json({ message: process.env.FLAG, type: "pwned" })
          : res.json({
              message:
                "Successfully uploaded files, thanks for sharing a true .png/.jpg file ;) ",
              type: "success",
            });
      }
    });
  });
}

app.get("/ping", (req, res) => {
  return res.json({ message: "pong" });
});

app.listen(5000, () => {
  console.log(`Server started...`);
});
