# Incognito
![Categorie](https://img.shields.io/badge/Category-Digtal%20Forensics-red?style=for-the-badge) ![Level](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)

![tags](https://img.shields.io/badge/Tag-Network%20Traffic-blue)

## Description
> Someone used my incognito tab to download something from the Internet, but he didn’t notice Wireshark running in the background!
> 
> [Link to File](https://drive.google.com/file/d/19Y1AavMD4xLOem2bJYQrvArXP3Hsd2xn/view?usp=sharing)
>
> SHA1: 44efbd090a5e673e035a48a79e82f774c7c0f64b

## Steps to solve

> Open the file in Wireshark
> File Menu > Export Objects > HTTP
> You will find download.zip archive
> Extract and check flag.png

## Questions

Tools: **Wireshark**.

1. How many packets does the capture have? **50pts**

`25985`

2. At what time was the first packet captured? (YYYY-MM-DD HH:MM:SS UTC) **50pts**

`2022-08-31 11:27:21 UTC`

3. What is the interface name that is being captured? **100pts**

`vEthernet (WSL)`

4. What is the Vendor of the active computer? **200pts**

`Microsoft Corporation`

5. What browser is being used in the capture? (Browser Version) **100pts**

`Firefox 104`

6. Can you find the download content? (Securinets{...}) **200pts**

`Securinets{n3v3r_7ru5t_1ncogn1t0}`
