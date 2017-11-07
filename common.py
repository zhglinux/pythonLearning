import numpy as np
import pandas as pd
import visuals as vs

data = pd.read_csv('bj_housing.csv')
prices = data['MEDV']
features = data.drop('MEDV', axis=1)

# 完成
print "Boston housing dataset has {} data points with {} variables each.".format(*data.shape)


#目标：计算价值的最小值
minimum_price =  np.min(prices)  #None

#目标：计算价值的最大值
maximum_price = np.max(prices)  #None

#目标：计算价值的平均值
mean_price = np.mean(prices)  #None

#目标：计算价值的中值
median_price = np.median(prices) # None

#目标：计算价值的标准差
std_price = np.std(prices) #None

#目标：输出计算的结果
print "Statistics for Boston housing dataset:\n"
print "Minimum price: ${:,.2f}".format(minimum_price)
print "Maximum price: ${:,.2f}".format(maximum_price)
print "Mean price: ${:,.2f}".format(mean_price)
print "Median price ${:,.2f}".format(median_price)
print "Standard deviation of prices: ${:,.2f}".format(std_price)


# TODO 2

# 提示： 导入train_test_split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    features, prices, test_size=0.2, random_state=0) # None
print y_train,y_test

# 提示： 导入r2_score
from sklearn.metrics import r2_score


def performance_metric(y_true, y_predict):
    """计算并返回预测值相比于预测值的分数"""
    score = r2_score(y_true, y_predict)
    print score
    return score

# 计算这个模型的预测结果的决定系数
score = performance_metric([3, -0.5, 2, 7, 4.2], [2.5, 0.0, 2.1, 7.8, 5.3])
print "Model has a coefficient of determination, R^2, of {:.3f}.".format(score)

# 提示: 导入 'KFold' 'DecisionTreeRegressor' 'make_scorer' 'GridSearchCV'

from sklearn.metrics import fbeta_score, make_scorer
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV, KFold


def fit_model(X, y):
    """ 基于输入数据 [X,y]，利于网格搜索找到最优的决策树模型"""

    cross_validator = KFold(n_splits=5)

    regressor = DecisionTreeRegressor(random_state=5)

    params = {'max_depth': range(1, 11)}

    scoring_fnc = make_scorer(performance_metric)

    grid = GridSearchCV(regressor, params, scoring_fnc, cv=cross_validator)
    #    GridSearchCV(regressor, param_grid = params, scoring = scoring_fnc, cv = cross_validator)

    # 基于输入数据 [X,y]，进行网格搜索
    grid = grid.fit(X, y)

    print '---below---'

    #     print pd.DataFrame(grid.cv_results_)

    print '---above---'

    # 返回网格搜索后的最优模型
    return grid.best_estimator_


# 基于训练数据，获得最优模型
optimal_reg = fit_model(X_train, y_train)

# 输出最优模型的 'max_depth' 参数
print "Parameter 'max_depth' is {} for the optimal model.".format(optimal_reg.get_params()['max_depth'])

predicted_price = optimal_reg.predict(X_test)
for i, price in enumerate(predicted_price):
    print "Predicted selling price for Client {}'s home: ${:,.2f}".format(i + 1, price)

r2 = performance_metric(y_test, predicted_price)

print "Optimal model has R^2 score {:,.2f} on test data".format(r2)



# 请先注释掉 fit_model 函数里的所有 print 语句
vs.PredictTrials(features, prices, fit_model, client_data)

