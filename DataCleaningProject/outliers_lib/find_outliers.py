def outliers_iqr(data,feature):
    x=data[feature]
    quantile_1, quantile_3=x.quantile(0.25), x.quantile(0.75)
    iqr=quantile_3-quantile_1
    lower_bound=quantile_1-(iqr*1.5)
    upper_bound=quantile_3+(iqr*1.5)
    outliers=data[(x<lower_bound)|(x>upper_bound)]
    cleaned=data[(x>lower_bound)&(x<upper_bound)]
    return outliers, cleaned
def outliers_z_score(data,feature,log_scale=False):
    if log_scale:
        x=np.log(data[feature])
    else:
        x=data[feature]
    mu=x.mean()
    sigma=x.std()
    lower_bound=mu-3*sigma
    upper_bound=mu+3*sigma
    outliers=data[(x<lower_bound)|(x>upper_bound)]
    cleaned=data[(x>lower_bound)&(x<upper_bound)]
    return outliers, cleaned