import { network } from "hardhat";
import { DeployFunction } from "hardhat-deploy/dist/types";
import { developmentChains } from "../helper-hardhat-config";
import { verify } from "../utils/verify";



const DeployGreedyRobot: DeployFunction = async ({ getNamedAccounts, deployments }) => {

    const { deployer } = await getNamedAccounts();
    const { deploy, log } = deployments;
    log("-------------------")
    const args: any = [];

    const GreedyRobot = await deploy("GreedyRobot", {
        from: deployer,
        log: true,
        waitConfirmations: 1,
        
    })

    if (!developmentChains.includes(network.name)) {
        await verify(GreedyRobot.address, args)
    }

}

export default DeployGreedyRobot;
DeployGreedyRobot.tags=["all",]