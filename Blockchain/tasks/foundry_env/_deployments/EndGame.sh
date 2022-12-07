forge create --rpc-url https://eth-rinkeby.alchemyapi.io/v2/70KesqNGVj_x7U7waDWhpODHHEvzVg3O \
--private-key _PRIVATE_KEY src/EndGame.sol:EndGame \
--etherscan-api-key _ETHERSCAN_API_KEY \
--verify > test_file.txt
ADDRESS=`cat test_file.txt | grep Deployed | cut -d ' ' -f3`
echo "NEXT_PUBLIC_ADDRESS= $ADDRESS" >> ./fronts/EndGame/current_contract.txt
rm -rf ./test_file.txt
cd ./fronts/CrazyGambler/
vercel env add NEXT_PUBLIC_CONTRACT_ADDRESS preview < current_contract.txt
vercel deploy --prod


