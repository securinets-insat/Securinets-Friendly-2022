// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "forge-std/Test.sol";
import "forge-std/console.sol";
import "../src/NoManLand.sol";
import "../src/NoManLandSolver.sol";

contract TestingNoManLand is Test {

    NoManLand victimContract;
    Solver solverContract;

    function setUp() public {
        victimContract = new NoManLand();
        solverContract=new Solver(address(victimContract));
    }

    function testExploit() public{
        console.log(address(this));
        console.log(msg.sender);
        bool res =solverContract.getFlag();
        console.log(res);

        assert(res==true);
    }


}