// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

contract NoManLand {
    mapping(address => bool) flagHolders;

    event WonFlag(address indexed);

    function sendFlag() public returns (bool) {
        require(
            tx.origin != msg.sender,
            "Hey you are not getting the point here"
        );
        flagHolders[tx.origin] = true;
        emit WonFlag(tx.origin);
        return true;
    }

    function canGetFlag(address playerAddress) public view returns (bool) {
        
        return flagHolders[playerAddress];
    }
}
