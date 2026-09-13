#!/bin/bash
# add-submodules.sh
# Helper script to add and initialize the five lottery project submodules locally.
# Run this in a local clone of your repository (US3456H/3456).

set -euo pipefail

git submodule add https://github.com/CorvusCodex/LotteryAi.git external/LotteryAi
git submodule add https://github.com/bartoszclapinski/LotteryLAB.git external/LotteryLAB
git submodule add https://github.com/JeffMv/Lofea.git external/Lofea
git submodule add https://github.com/Ahmad-Alam/Lottery-Prediction.git external/Lottery-Prediction
git submodule add https://github.com/Callam7/LottoPipeline.git external/LottoPipeline

# Initialize and fetch
git submodule update --init --recursive

echo "Submodules added and initialized. Remember to commit the .gitmodules and submodule pointers:"

echo "  git add .gitmodules external/*"
echo "  git commit -m \"Add lottery projects as submodules\""
echo "  git push origin main"
