import { expect } from "chai";
import { Signer } from "ethers";
import { deployments, ethers, getNamedAccounts } from "hardhat";
import { GreedyRobot, GreedyRobot__factory } from "../typechain-types";

describe("Greedy Robot", function () {
    let GreedyRobotContract: GreedyRobot;
    let GreedyRobotFactory: GreedyRobot__factory;
    let deployer: string;
    let deployerSigner: Signer;
    let anotherSigner: Signer;

    beforeEach(async () => {
        await deployments.fixture("all")
        deployer = (await getNamedAccounts()).deployer;
        [deployerSigner, anotherSigner] = await ethers.getSigners();


        GreedyRobotFactory = await ethers.getContractFactory("GreedyRobot");
        GreedyRobotContract = await GreedyRobotFactory.deploy()

        await GreedyRobotContract.deployed()
    })

    it("Should deploy GreedyRobot", async () => {
        expect(GreedyRobotContract.address).to.properAddress;
    })

    it("Should have a minimum contribution of 0.1 ether", async () => {
        expect(GreedyRobotContract.MINIMUM_CONTRIBUTION()).to.eventually.equal(ethers.utils.parseEther("0.1"))
    })

    it("Should revert when not respecting the min contribution", async () => {
        await expect(deployerSigner.sendTransaction({
            to: GreedyRobotContract.address,
            value: ethers.utils.parseEther("0.01"),
            gasLimit: 300000
        })).to.be.revertedWithoutReason

        expect((await ethers.provider.getBalance(GreedyRobotContract.address)).toString()).to.equal('0')
    })

    it("Working finely when contributed", async () => {
        await expect(deployerSigner.sendTransaction({
            to: GreedyRobotContract.address, value: ethers.utils.parseEther("0.1"),
            gasLimit: 300000
        })).to.be.fulfilled;

        const currentContractBalance = (await ethers.provider.getBalance(GreedyRobotContract.address)).toString()
        expect(currentContractBalance).to.equal(ethers.utils.parseEther("0.1").toString())

        const canPass = await GreedyRobotContract.canPass(deployerSigner.getAddress());
        expect(canPass).to.be.true;
    })

    it('Only owner can withdraw', async () => {
        await expect(GreedyRobotContract.connect(anotherSigner).widthdraw()).to.be.reverted;
        await expect(GreedyRobotContract.widthdraw()).to.be.fulfilled;
        await expect(ethers.provider.getBalance(GreedyRobotContract.address)).to.eventually.equal(0)
    })

})


