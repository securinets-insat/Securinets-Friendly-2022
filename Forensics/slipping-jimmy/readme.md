# Slipping Jimmy
![Categorie](https://img.shields.io/badge/Category-Digtal%20Forensics-red?style=for-the-badge) ![Level](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)

![tags](https://img.shields.io/badge/Tag-Network%20Malware%20Analysis-blue)

## Description
> A PayPal monthly statement email was sent to a mailbox, it leads to a phishing page that asks the user to login first to download a malware disguised as a statement document.
> 
> [Link to File](https://drive.google.com/file/d/1IoTIMN5J7EQZxEPut0JblkbLDAojO-R-/view?usp=sharing)
>
> SHA1: 0d615e81e16ce97f59fccd4e7ab0acd21674e827

## Questions

Tools: **Wireshark**, **VirusTotal**

1. How long did the operation take in seconds? **50pts**

`58`

2. What is the victim's IP address? **50pts**
   
`192.168.182.132`

3. What is the victim's OS? **100pts**

`Windows XP`

*Win NT5.1 is XP - from the User Agent*

4. What is the attacker's webserver url (without http://)? **50pts**

`b68d-102-159-93-234.eu.ngrok.io`

5. Which software run the webserver that hosts the phishing page? **100pts**

*Hint/Placeholder: Si............ ...........10*

`SimpleHTTP/0.6 Python/3.8.10`

6. What are the PayPal stolen credentials? (email:password) **150pts**

`jamesmcgill@aol.com:Worlds2ndBe$tLawy3r`

7. What is the md5 hash of the malicious file? **200pts**
   
`d01b417a7922cda8a3211c9dd8309306`

8. What is the name of the malware according to Comodo? **200pts**

`Malware@#dvt1zjhgifb1`

9. Can you find the creation time of the malware? (YYYY-MM-DD HH:MM:SS UTC) **200pts**

`2020-07-24 04:07:50 UTC`

10.  Which IP is being contacted from the malware? **300pts**

`217.8.117.52`
