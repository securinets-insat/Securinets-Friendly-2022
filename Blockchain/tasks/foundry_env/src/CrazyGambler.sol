// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.6.0;

contract CrazyGambler {
    mapping(address => bool) public gotTrial;
    mapping(address => bool) flagHolders;
    mapping(address => uint256) public gamblersCredit;

    event WonFlag(address indexed);

    function _rollDice() internal view returns (uint256) {
        uint256 blockNo = block.number - 1;
        uint256 diceRes = uint256(blockhash(blockNo)) % 3;
        return diceRes;
    }

    function trialCredit() public {
        require(!gotTrial[msg.sender], "You already got your trial credits");
        gamblersCredit[msg.sender] += 7;
    }

    function gamble(address ownerAddress) public {
        // Fuck off, No need to emit event again.
        require(!flagHolders[ownerAddress]);
        uint256 roll = _rollDice();

        if (roll == 0) {
            gamblersCredit[msg.sender] += 1;
        } else {
            gamblersCredit[msg.sender] = 0;
        }

        if (gamblersCredit[msg.sender] == 17) {
            flagHolders[ownerAddress] = true;

            // Good bye gambler :)
            gamblersCredit[msg.sender] = 0;
            emit WonFlag(ownerAddress);
        }
    }

    function canGetFlag(address playerAddress) public view returns (bool) {
        return flagHolders[playerAddress];
    }
}
