import { ethers } from "ethers";
import ABI from "../../ABI/GreedyRobot.json";
export default async function handler(req, res) {
    if (req.method === 'POST') {
        if (!req.body.address)
            return res.status(400).json({ error: "address is required" });
        const provider = new ethers.providers.AlchemyProvider("goerli", process.env.ALCHEMY_API_KEY)
        const contract = new ethers.Contract("0x79089d5B521030852EdEEeF47A3cD726F3d59e7b", ABI, provider)

        const canPass = await contract.canPass(req.body.address);
        let response = { canPass }
        if (canPass) {
            response.flag = process.env.FLAG;
        }
        return res.status(200).json(response);
    }

    return res.status(404);
}
