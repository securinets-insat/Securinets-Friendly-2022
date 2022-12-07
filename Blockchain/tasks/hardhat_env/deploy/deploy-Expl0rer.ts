import { assert } from "chai";
import { network } from "hardhat";
import { DeployFunction } from "hardhat-deploy/dist/types";
import { developmentChains } from "../helper-hardhat-config";
import { verify } from "../utils/verify";



const DeployExplorer: DeployFunction = async ({ getNamedAccounts, deployments }) => {
    console.log(process.env.FLAG)
    assert(process.env.FLAG, "FLAG is not set")

    const { deployer } = await getNamedAccounts();
    const { deploy, log } = deployments;
    log("-------------------")
    const args: any = [process.env.FLAG || ""];

    const Expl0rer = await deploy("Expl0rer", {
        from: deployer,
        args,
        log: true,
        waitConfirmations: 1
    })

    if (!developmentChains.includes(network.name)) {
        await verify(Expl0rer.address, args)
    }

}

export default DeployExplorer;
DeployExplorer.tags = ["all" ,"explorer"]