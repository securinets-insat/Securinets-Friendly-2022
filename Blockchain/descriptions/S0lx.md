# S0lx

`CONTRACT Code`

```js
// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

contract S0lx {
    address public owner;
    string public S;
    string public O;
    string public L;
    string public immutable X="COntr4cts_";

    constructor() {
        owner = msg.sender;
    }

    function question() public pure returns (string memory) {
        return "What is the answer to life, the universe and everything?";
    }

    function answer() public returns (string memory) {
        S = "S0l1dItY_";
        O = "securinets{";
        L = "ARe_4w3s0m3}";
        return string(abi.encodePacked(O,S, X, L));
    }
}
```

## Description

The last reminants of the temple of S0l were found few days ago. It was a moonless night when the mountain shattered to reveal the old monument.
The archaelogies found some old runes on the walls of the temple. They were written in a language that was not known to the world.
They say by decoding the runes you can unlock some inhuman powers.

Decode the contract

> Flag `securinets{S0l1dItY_COntr4cts_ARe_4w3s0m3}`
