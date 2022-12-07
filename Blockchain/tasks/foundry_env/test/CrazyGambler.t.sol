// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.6.0;

import "forge-std/Test.sol";
import "forge-std/console.sol";
import "../src/CrazyGambler.sol";

contract TestingGambler is Test {
    CrazyGambler crazyGambler;

    // Solver solverContract;

    function setUp() public {
        crazyGambler = new CrazyGambler();
    }

    function testExploit() public {
        // crazyGambler.trialCredit();
        // while (!crazyGambler.canGetFlag(address(this))) {
        //     if (crazyGambler._rollDice() == 0) {
        //         crazyGambler.gamble();
        //     }
        // }
        // assert(crazyGambler.canGetFlag(address(this)));
    }
}

