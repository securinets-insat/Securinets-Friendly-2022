import { ethers } from "hardhat";
import { Expl0rer__factory, GreedyRobot__factory, Int3r4ct, Int3r4ct__factory } from "../typechain-types";
import { verify } from "../utils/verify";


async function main() {
  console.log(process.env.FLAG)

  // Deploy & verify Expl0rer
  const Expl0rerFactory: Expl0rer__factory = await ethers.getContractFactory("Expl0rer");
  let Expl0rerContract = await Expl0rerFactory.deploy(process.env.FLAG || "")
  Expl0rerContract = await Expl0rerContract.deployed()
  console.log("Expl0rer deployed to:", Expl0rerContract.address);

  await verify(Expl0rerContract.address, [process.env.FLAG || ""]);

  console.log('verified')

  // Deploy Greedy Robot
  const GreedyRobotFactory: GreedyRobot__factory = await ethers.getContractFactory("GreedyRobot");
  let GreedyRobot = await GreedyRobotFactory.deploy()
  GreedyRobot = await GreedyRobot.deployed()

  console.log("Greedy Robot deployed to:", GreedyRobot.address);



  //  Deploy Int3ract
  const Int3ractFactory: Int3r4ct__factory = await ethers.getContractFactory("Int3r4ct");
  let Int3ractContract: Int3r4ct = await Int3ractFactory.deploy()
   Int3ractContract= await Int3ractContract.deployed()

  console.log("Int3r4ct deployed to:", Int3ractContract.address);



}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
