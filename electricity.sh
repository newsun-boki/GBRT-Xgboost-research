rm -rf electricity_train
mkdir ./electricity_train
cd ./electricity_train || exit
echo  "start training"
env > env.log
python ../xgboostWB_electricity.py > eval.log 2>&1 &
cd ../