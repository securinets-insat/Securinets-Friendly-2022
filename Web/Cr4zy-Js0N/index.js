const express = require("express");

const app = express();
1;
require("dotenv").config();

const PORT = process.env.PORT || 5001;

console.log(__dirname);

app.use(express.static("public"));

app.use(express.json());

app.post("/", async (req, res) => {
  if (verifyRequestBody(req.body)) {
    return res.json({ flag: process.env.FLAG });
  }
  return res.json({
    toto: {
      toto: {
        toto: {
          toto: {
            toto: {
              toto: {
                toto: {
                  toto: {
                    toto: {
                      toto: {
                        toto: {
                          toto: {
                            toto: {
                              toto: {
                                toto: {
                                  toto: {
                                    toto: {
                                      toto: {
                                        toto: {
                                          toto: {
                                            toto: {
                                              toto: {
                                                toto: {
                                                  toto: {
                                                    toto: {
                                                      toto_titao: "wrong !",
                                                    },
                                                  },
                                                },
                                              },
                                            },
                                          },
                                        },
                                      },
                                    },
                                  },
                                },
                              },
                            },
                          },
                        },
                      },
                    },
                  },
                },
              },
            },
          },
        },
      },
    },
  });
});

app.get("/", (_, res) => {
  return res.sendFile(__dirname + "/index.html");
});

function verifyRequestBody(body) {
  if (body && body.answers && body?.answers.length === 3) {
    if (
      body.answers[0]["Gate One"] === "Man" &&
      body.answers[1]["Gate Two"] &&
      body.answers[2]["Gate Three"] === 12
    ) {
      return true;
    }
  }

  return false;
}

app.listen(PORT, () => {
  console.log(`port open on ${PORT}`);
});
