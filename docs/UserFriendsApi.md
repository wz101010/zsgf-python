# ZSGF.Client.UserFriendsApi

All URIs are relative to *https://api-dev.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_common_interests**](UserFriendsApi.md#user_common_interests) | **GET** /UserFriends/{appKey}/CommonInterests | 推荐相似兴趣用户
[**user_follow_user**](UserFriendsApi.md#user_follow_user) | **POST** /UserFriends/{appKey}/Follower/{userId} | 添加关注
[**user_follower_put**](UserFriendsApi.md#user_follower_put) | **PUT** /UserFriends/{appKey}/Follower/{id} | 刷新粉丝数据
[**user_followers**](UserFriendsApi.md#user_followers) | **GET** /UserFriends/{appKey}/Followers | 获取粉丝列表
[**user_following**](UserFriendsApi.md#user_following) | **GET** /UserFriends/{appKey}/Following | 获取关注列表 / 判断是否关注
[**user_friends_near_by**](UserFriendsApi.md#user_friends_near_by) | **GET** /UserFriends/{appKey}/NearBy | 推荐附近用户
[**user_mutual_followers**](UserFriendsApi.md#user_mutual_followers) | **GET** /UserFriends/{appKey}/MutualFollowers | 推荐共同粉丝用户
[**user_mutual_followings**](UserFriendsApi.md#user_mutual_followings) | **GET** /UserFriends/{appKey}/MutualFollowings | 推荐共同关注用户
[**user_profile_by_id**](UserFriendsApi.md#user_profile_by_id) | **GET** /UserFriends/{appKey}/Profile/{userId} | 获取用户资料
[**user_unfollow_user**](UserFriendsApi.md#user_unfollow_user) | **DELETE** /UserFriends/{appKey}/Follower/{userId} | 取消关注


# **user_common_interests**
> UserCommonInterestsResultApiResponse user_common_interests(app_key, tag=tag, skip=skip, take=take, user_id=user_id)

推荐相似兴趣用户

推荐有共同爱好的用户

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.user_common_interests_result_api_response import UserCommonInterestsResultApiResponse
from ZSGF.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-dev.zashigaofa.cn
# See configuration.py for a list of all supported configuration parameters.
configuration = ZSGF.Client.Configuration(
    host = "https://api-dev.zashigaofa.cn"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = ZSGF.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ZSGF.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ZSGF.Client.UserFriendsApi(api_client)
    app_key = 'app_key_example' # str | 
    tag = 'tag_example' # str | 兴趣标签 (optional)
    skip = 0 # int | 跳过的记录数 (optional) (default to 0)
    take = 10 # int | 获取的记录数 (optional) (default to 10)
    user_id = '' # str |  (optional) (default to '')

    try:
        # 推荐相似兴趣用户
        api_response = api_instance.user_common_interests(app_key, tag=tag, skip=skip, take=take, user_id=user_id)
        print("The response of UserFriendsApi->user_common_interests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFriendsApi->user_common_interests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **tag** | **str**| 兴趣标签 | [optional] 
 **skip** | **int**| 跳过的记录数 | [optional] [default to 0]
 **take** | **int**| 获取的记录数 | [optional] [default to 10]
 **user_id** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UserCommonInterestsResultApiResponse**](UserCommonInterestsResultApiResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_follow_user**
> BooleanApiResponse user_follow_user(user_id, app_key, from_user_id=from_user_id)

添加关注

关注指定用户

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-dev.zashigaofa.cn
# See configuration.py for a list of all supported configuration parameters.
configuration = ZSGF.Client.Configuration(
    host = "https://api-dev.zashigaofa.cn"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = ZSGF.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ZSGF.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ZSGF.Client.UserFriendsApi(api_client)
    user_id = 56 # int | 要关注的用户ID
    app_key = 'app_key_example' # str | 
    from_user_id = 'from_user_id_example' # str |  (optional)

    try:
        # 添加关注
        api_response = api_instance.user_follow_user(user_id, app_key, from_user_id=from_user_id)
        print("The response of UserFriendsApi->user_follow_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFriendsApi->user_follow_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| 要关注的用户ID | 
 **app_key** | **str**|  | 
 **from_user_id** | **str**|  | [optional] 

### Return type

[**BooleanApiResponse**](BooleanApiResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_follower_put**
> BooleanApiResponse user_follower_put(id, app_key, follower_put_model=follower_put_model)

刷新粉丝数据

根据粉丝ID更新粉丝信息

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.follower_put_model import FollowerPutModel
from ZSGF.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-dev.zashigaofa.cn
# See configuration.py for a list of all supported configuration parameters.
configuration = ZSGF.Client.Configuration(
    host = "https://api-dev.zashigaofa.cn"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = ZSGF.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ZSGF.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ZSGF.Client.UserFriendsApi(api_client)
    id = 56 # int | 粉丝ID
    app_key = 'app_key_example' # str | 
    follower_put_model = ZSGF.Client.FollowerPutModel() # FollowerPutModel | 更新粉丝的请求参数 (optional)

    try:
        # 刷新粉丝数据
        api_response = api_instance.user_follower_put(id, app_key, follower_put_model=follower_put_model)
        print("The response of UserFriendsApi->user_follower_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFriendsApi->user_follower_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 粉丝ID | 
 **app_key** | **str**|  | 
 **follower_put_model** | [**FollowerPutModel**](FollowerPutModel.md)| 更新粉丝的请求参数 | [optional] 

### Return type

[**BooleanApiResponse**](BooleanApiResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_followers**
> UserFollowersResultApiResponse user_followers(app_key, tag=tag, status=status, target_user_id=target_user_id, skip=skip, take=take, user_id=user_id)

获取粉丝列表

根据条件获取我的粉丝列表

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.user_followers_result_api_response import UserFollowersResultApiResponse
from ZSGF.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-dev.zashigaofa.cn
# See configuration.py for a list of all supported configuration parameters.
configuration = ZSGF.Client.Configuration(
    host = "https://api-dev.zashigaofa.cn"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = ZSGF.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ZSGF.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ZSGF.Client.UserFriendsApi(api_client)
    app_key = 'app_key_example' # str | 
    tag = 'tag_example' # str | 标签 (optional)
    status = 'status_example' # str | 状态 (optional)
    target_user_id = 0 # int | 指定用户的粉丝 (optional) (default to 0)
    skip = 0 # int | 跳过的记录数 (optional) (default to 0)
    take = 10 # int | 获取的记录数 (optional) (default to 10)
    user_id = '' # str |  (optional) (default to '')

    try:
        # 获取粉丝列表
        api_response = api_instance.user_followers(app_key, tag=tag, status=status, target_user_id=target_user_id, skip=skip, take=take, user_id=user_id)
        print("The response of UserFriendsApi->user_followers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFriendsApi->user_followers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **tag** | **str**| 标签 | [optional] 
 **status** | **str**| 状态 | [optional] 
 **target_user_id** | **int**| 指定用户的粉丝 | [optional] [default to 0]
 **skip** | **int**| 跳过的记录数 | [optional] [default to 0]
 **take** | **int**| 获取的记录数 | [optional] [default to 10]
 **user_id** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UserFollowersResultApiResponse**](UserFollowersResultApiResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_following**
> BooleanApiResponse user_following(app_key, tag=tag, status=status, target_user_id=target_user_id, skip=skip, take=take, check_user_id=check_user_id, only_ids=only_ids, user_id=user_id)

获取关注列表 / 判断是否关注

根据条件获取我的关注列表，或判断是否关注某个用户

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-dev.zashigaofa.cn
# See configuration.py for a list of all supported configuration parameters.
configuration = ZSGF.Client.Configuration(
    host = "https://api-dev.zashigaofa.cn"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = ZSGF.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ZSGF.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ZSGF.Client.UserFriendsApi(api_client)
    app_key = 'app_key_example' # str | 
    tag = 'tag_example' # str | 用于过滤关注列表的标签（可选）。 (optional)
    status = 'status_example' # str | 用于过滤关注列表的状态（可选）。 (optional)
    target_user_id = 0 # int | 指定用户的关注记录，如果不提供则默认为当前用户的关注。 (optional) (default to 0)
    skip = 0 # int | 跳过的记录数，用于分页（默认0）。 (optional) (default to 0)
    take = 10 # int | 获取的记录数，用于分页（默认10）。 (optional) (default to 10)
    check_user_id = 56 # int | 要判断是否关注的目标用户ID。如果提供此参数，方法将返回一个布尔值，表示当前用户是否关注该目标用户。 (optional)
    only_ids = False # bool | 是否只返回关注用户的ID集合，默认为false（即返回完整的关注用户信息）。 (optional) (default to False)
    user_id = '' # str |  (optional) (default to '')

    try:
        # 获取关注列表 / 判断是否关注
        api_response = api_instance.user_following(app_key, tag=tag, status=status, target_user_id=target_user_id, skip=skip, take=take, check_user_id=check_user_id, only_ids=only_ids, user_id=user_id)
        print("The response of UserFriendsApi->user_following:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFriendsApi->user_following: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **tag** | **str**| 用于过滤关注列表的标签（可选）。 | [optional] 
 **status** | **str**| 用于过滤关注列表的状态（可选）。 | [optional] 
 **target_user_id** | **int**| 指定用户的关注记录，如果不提供则默认为当前用户的关注。 | [optional] [default to 0]
 **skip** | **int**| 跳过的记录数，用于分页（默认0）。 | [optional] [default to 0]
 **take** | **int**| 获取的记录数，用于分页（默认10）。 | [optional] [default to 10]
 **check_user_id** | **int**| 要判断是否关注的目标用户ID。如果提供此参数，方法将返回一个布尔值，表示当前用户是否关注该目标用户。 | [optional] 
 **only_ids** | **bool**| 是否只返回关注用户的ID集合，默认为false（即返回完整的关注用户信息）。 | [optional] [default to False]
 **user_id** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**BooleanApiResponse**](BooleanApiResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_friends_near_by**
> UserFriendsNearByResultApiResponse user_friends_near_by(longitude, latitude, app_key, country=country, state=state, city=city, district=district, gender=gender, age_s=age_s, age_e=age_e, tag=tag, distance=distance, skip=skip, take=take, user_id=user_id)

推荐附近用户

根据地理位置坐标和多种筛选条件，查询附近满足条件的用户列表，支持分页和按距离排序。
地理位置查询使用MySQL的ST_Distance_Sphere函数计算球面距离。
注意：longitude为经度(X轴)，latitude为纬度(Y轴)，参数顺序与常规坐标系一致

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.user_friends_near_by_result_api_response import UserFriendsNearByResultApiResponse
from ZSGF.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-dev.zashigaofa.cn
# See configuration.py for a list of all supported configuration parameters.
configuration = ZSGF.Client.Configuration(
    host = "https://api-dev.zashigaofa.cn"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = ZSGF.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ZSGF.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ZSGF.Client.UserFriendsApi(api_client)
    longitude = 3.4 # float | 当前用户经度坐标(WGS84坐标系)
    latitude = 3.4 # float | 当前用户纬度坐标(WGS84坐标系)
    app_key = 'app_key_example' # str | 
    country = 'country_example' # str | 国家过滤条件（精确匹配） (optional)
    state = 'state_example' # str | 省份过滤条件（精确匹配） (optional)
    city = 'city_example' # str | 城市过滤条件（精确匹配） (optional)
    district = 'district_example' # str | 区县过滤条件（精确匹配） (optional)
    gender = 'gender_example' # str | 性别过滤条件（可选值示例：Male/Female/Other） (optional)
    age_s = 56 # int | 年龄起始范围（包含，0表示不限制） (optional)
    age_e = 56 # int | 年龄结束范围（包含，0表示不限制） (optional)
    tag = 'tag_example' # str | 兴趣标签过滤（支持模糊匹配，如：\"运动\"） (optional)
    distance = 0 # int | 搜索半径（单位：米，0表示不限制距离） (optional) (default to 0)
    skip = 0 # int | 跳过的记录数（分页起始位置，默认0） (optional) (default to 0)
    take = 10 # int | 获取的记录数（分页大小，默认10，最大100） (optional) (default to 10)
    user_id = '' # str |  (optional) (default to '')

    try:
        # 推荐附近用户
        api_response = api_instance.user_friends_near_by(longitude, latitude, app_key, country=country, state=state, city=city, district=district, gender=gender, age_s=age_s, age_e=age_e, tag=tag, distance=distance, skip=skip, take=take, user_id=user_id)
        print("The response of UserFriendsApi->user_friends_near_by:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFriendsApi->user_friends_near_by: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **longitude** | **float**| 当前用户经度坐标(WGS84坐标系) | 
 **latitude** | **float**| 当前用户纬度坐标(WGS84坐标系) | 
 **app_key** | **str**|  | 
 **country** | **str**| 国家过滤条件（精确匹配） | [optional] 
 **state** | **str**| 省份过滤条件（精确匹配） | [optional] 
 **city** | **str**| 城市过滤条件（精确匹配） | [optional] 
 **district** | **str**| 区县过滤条件（精确匹配） | [optional] 
 **gender** | **str**| 性别过滤条件（可选值示例：Male/Female/Other） | [optional] 
 **age_s** | **int**| 年龄起始范围（包含，0表示不限制） | [optional] 
 **age_e** | **int**| 年龄结束范围（包含，0表示不限制） | [optional] 
 **tag** | **str**| 兴趣标签过滤（支持模糊匹配，如：\&quot;运动\&quot;） | [optional] 
 **distance** | **int**| 搜索半径（单位：米，0表示不限制距离） | [optional] [default to 0]
 **skip** | **int**| 跳过的记录数（分页起始位置，默认0） | [optional] [default to 0]
 **take** | **int**| 获取的记录数（分页大小，默认10，最大100） | [optional] [default to 10]
 **user_id** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UserFriendsNearByResultApiResponse**](UserFriendsNearByResultApiResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 返回推荐用户列表数据 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_mutual_followers**
> UserMutualFollowersResultApiResponse user_mutual_followers(app_key, skip=skip, take=take, user_id=user_id)

推荐共同粉丝用户

推荐有共同粉丝的用户

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.user_mutual_followers_result_api_response import UserMutualFollowersResultApiResponse
from ZSGF.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-dev.zashigaofa.cn
# See configuration.py for a list of all supported configuration parameters.
configuration = ZSGF.Client.Configuration(
    host = "https://api-dev.zashigaofa.cn"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = ZSGF.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ZSGF.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ZSGF.Client.UserFriendsApi(api_client)
    app_key = 'app_key_example' # str | 
    skip = 0 # int | 跳过的记录数 (optional) (default to 0)
    take = 10 # int | 获取的记录数 (optional) (default to 10)
    user_id = '' # str |  (optional) (default to '')

    try:
        # 推荐共同粉丝用户
        api_response = api_instance.user_mutual_followers(app_key, skip=skip, take=take, user_id=user_id)
        print("The response of UserFriendsApi->user_mutual_followers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFriendsApi->user_mutual_followers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **skip** | **int**| 跳过的记录数 | [optional] [default to 0]
 **take** | **int**| 获取的记录数 | [optional] [default to 10]
 **user_id** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UserMutualFollowersResultApiResponse**](UserMutualFollowersResultApiResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_mutual_followings**
> UserMutualFollowingsResultApiResponse user_mutual_followings(app_key, skip=skip, take=take, user_id=user_id)

推荐共同关注用户

推荐有共同关注的用户

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.user_mutual_followings_result_api_response import UserMutualFollowingsResultApiResponse
from ZSGF.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-dev.zashigaofa.cn
# See configuration.py for a list of all supported configuration parameters.
configuration = ZSGF.Client.Configuration(
    host = "https://api-dev.zashigaofa.cn"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = ZSGF.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ZSGF.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ZSGF.Client.UserFriendsApi(api_client)
    app_key = 'app_key_example' # str | 
    skip = 0 # int | 跳过的记录数 (optional) (default to 0)
    take = 10 # int | 获取的记录数 (optional) (default to 10)
    user_id = '' # str |  (optional) (default to '')

    try:
        # 推荐共同关注用户
        api_response = api_instance.user_mutual_followings(app_key, skip=skip, take=take, user_id=user_id)
        print("The response of UserFriendsApi->user_mutual_followings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFriendsApi->user_mutual_followings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **skip** | **int**| 跳过的记录数 | [optional] [default to 0]
 **take** | **int**| 获取的记录数 | [optional] [default to 10]
 **user_id** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**UserMutualFollowingsResultApiResponse**](UserMutualFollowingsResultApiResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_profile_by_id**
> GetUserProfileResultApiResponse user_profile_by_id(user_id, app_key)

获取用户资料

用于他人主页展示

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.get_user_profile_result_api_response import GetUserProfileResultApiResponse
from ZSGF.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-dev.zashigaofa.cn
# See configuration.py for a list of all supported configuration parameters.
configuration = ZSGF.Client.Configuration(
    host = "https://api-dev.zashigaofa.cn"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = ZSGF.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ZSGF.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ZSGF.Client.UserFriendsApi(api_client)
    user_id = 56 # int | 用户ID
    app_key = 'app_key_example' # str | 

    try:
        # 获取用户资料
        api_response = api_instance.user_profile_by_id(user_id, app_key)
        print("The response of UserFriendsApi->user_profile_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFriendsApi->user_profile_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| 用户ID | 
 **app_key** | **str**|  | 

### Return type

[**GetUserProfileResultApiResponse**](GetUserProfileResultApiResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_unfollow_user**
> BooleanApiResponse user_unfollow_user(user_id, app_key, from_user_id=from_user_id)

取消关注

取消关注指定用户

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-dev.zashigaofa.cn
# See configuration.py for a list of all supported configuration parameters.
configuration = ZSGF.Client.Configuration(
    host = "https://api-dev.zashigaofa.cn"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = ZSGF.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ZSGF.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ZSGF.Client.UserFriendsApi(api_client)
    user_id = 56 # int | 要取消关注的用户ID
    app_key = 'app_key_example' # str | 
    from_user_id = 'from_user_id_example' # str |  (optional)

    try:
        # 取消关注
        api_response = api_instance.user_unfollow_user(user_id, app_key, from_user_id=from_user_id)
        print("The response of UserFriendsApi->user_unfollow_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFriendsApi->user_unfollow_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| 要取消关注的用户ID | 
 **app_key** | **str**|  | 
 **from_user_id** | **str**|  | [optional] 

### Return type

[**BooleanApiResponse**](BooleanApiResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

