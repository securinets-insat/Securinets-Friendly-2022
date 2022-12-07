# !/bin/bash
forge create --rpc-url https://rinkeby.infura.io/v3/6b3d1bbb24f84624a8e2aaae46c1ec95 \
--private-key _PRIVATE_KEY src/CrazyGambler.sol:CrazyGambler \
--etherscan-api-key _ETHERSCAN_API_KEY \
--verify > test_file.txt

ADDRESS=`cat test_file.txt | grep Deployed | cut -d ' ' -f3`
echo "NEXT_PUBLIC_ADDRESS= $ADDRESS" >> ./fronts/CrazyGambler/current_contract.txt
rm -rf ./test_file.txt
cd ./fronts/CrazyGambler/
vercel env add NEXT_PUBLIC_CONTRACT_ADDRESS preview < current_contract.txt
vercel deploy --prod
r


