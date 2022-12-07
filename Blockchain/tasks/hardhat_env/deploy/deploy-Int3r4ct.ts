import { network } from "hardhat";
import { DeployFunction } from "hardhat-deploy/dist/types";
import { developmentChains } from "../helper-hardhat-config";
import { verify } from "../utils/verify";



const DeployGreedyRobot: DeployFunction = async ({ getNamedAccounts, deployments }) => {

    const { deployer } = await getNamedAccounts();
    const { deploy, log } = deployments;
    log("-------------------")
    const args: any = [];

    const Int3r4ct = await deploy("Int3r4ct", {
        from: deployer,
        log: true,
        waitConfirmations: 1,
    })

    if (!developmentChains.includes(network.name)) {
        await verify(Int3r4ct.address, args)
    }

}

export default DeployGreedyRobot;
DeployGreedyRobot.tags = ["all", "robot"]