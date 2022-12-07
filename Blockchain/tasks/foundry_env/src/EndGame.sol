// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.6.0;


contract EndGame {
    mapping(address => uint256) playersHealth;
    mapping(address => uint256) playersPoints;
    mapping(address => bool) players;
    mapping(address => bool) flagHolders;

    event WonFlag(address indexed);

    function joinedGame(address realPlayerAddress) public {
        require(
            !players[realPlayerAddress],
            "Player has already joined the game"
        );
        playersHealth[realPlayerAddress] = 1000;
        players[realPlayerAddress] = true;
    }

    function climbLeaderboard(uint256 tryhardCoeff, address realPlayerAddress)
        public
    {
        require(!flagHolders[msg.sender]);
        require(players[realPlayerAddress], "You are not a player");
        require(
            playersHealth[realPlayerAddress] - 100 * tryhardCoeff > 0,
            "Player is dead"
        );
        
        playersHealth[realPlayerAddress] -= 200 * tryhardCoeff;
        playersPoints[realPlayerAddress] += 100;

        if (playersPoints[realPlayerAddress] > 1000) {
            emit WonFlag(tx.origin);
            flagHolders[msg.sender]=true;
        }
    }

    function canGetFlag(address playerAddress) public view returns (bool) {
        return flagHolders[playerAddress];
    }
}
