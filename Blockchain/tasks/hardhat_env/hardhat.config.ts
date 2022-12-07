import * as dotenv from "dotenv"
import { HardhatUserConfig } from "hardhat/config";
import 'hardhat-abi-exporter';

import "@nomicfoundation/hardhat-toolbox";
import "@nomiclabs/hardhat-etherscan";
import "@nomiclabs/hardhat-waffle";
import "@typechain/hardhat";
import "hardhat-deploy";
import "hardhat-gas-reporter";
import "solidity-coverage";

dotenv.config();

const ALCHEMY_API_KEY = process.env.ALCHEMY_API_KEY || "";
const GOERLI_PRIVATE_KEY = process.env.GOERLI_PRIVATE_KEY || "";

const config: HardhatUserConfig = {
  abiExporter: [
    {
      path: './front/Int3ract-front/src/ABI',
      runOnCompile: true,
      clear: true,
      flat: true,
      only: [':Int3r4ct$'],
      spacing: 2,
      format: "json"
    },
    {
      path: './front/GreedyR0b0t-front/src/ABI',
      runOnCompile: true,
      clear: true,
      flat: true,
      only: [':GreedyRobot$'],
      spacing: 2,
      format: "json"
    }

  ],
  solidity: "0.8.9",
  etherscan: {
    apiKey: process.env.ETHERSCAN_API_KEY,
  },
  networks: {
    goerli: {
      url: `https://eth-goerli.alchemyapi.io/v2/${ALCHEMY_API_KEY}`,
      accounts: [GOERLI_PRIVATE_KEY],
    }

  },
  namedAccounts: {
    deployer: {
      default: 0,
    },
  },
};

export default config;
