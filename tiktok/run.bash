#!/bin/bash  
set -e

red=`tput setaf 5`
green=`tput setaf 2`
reset=`tput sgr0`

# cursor=0
hashtag="noacastillo"
# mkdir "data/${hashtag}"
for ((cursor = 1650; cursor <= 20000; cursor+=50))
do
  echo "${red} cursor  ${cursor} ...${reset}"
  sudo docker run -v TikTokApi --rm tiktokapi:latest python3 runrun.py $cursor $hashtag > "data/${hashtag}/${hashtag}-${cursor}.json"
done



# filename="test.abs"
# sudo docker run --rm -v "$PWD":/usr/src -w /usr/src abslang/absc:latest --erlang test.abs

# echo "${green}running program ...${reset}"
# echo "${green}___________________${reset}"
# sudo docker run --rm -v "$PWD":/usr/src -w /usr/src --entrypoint /usr/src/gen/erl/run abslang/absc
