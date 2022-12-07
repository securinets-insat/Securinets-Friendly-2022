// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

contract S0lx {
    address public owner;
    string public S;
    string public O;
    string public L;
    string public X;

    constructor() {
        owner = msg.sender;
    }

    function question() public pure returns (string memory) {
        return "What is the answer to life, the universe and everything?";
    }

    function answer() public returns (string memory) {
        S = "securinets{";
        O = "S0l1dItY_";
        L = "C0ntr4cts_";
        X = "ARe_4w3s0m3}";
        return string(abi.encodePacked(S, O, L, X));
    }
}
