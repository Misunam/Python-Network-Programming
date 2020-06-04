from geopy.geocoders import Nominatim
#地理位置信息库geopy 地理编码解析Nominatim

if __name__ == '__main__':
#自己的 __name__ 在自己用时就是 main，当自己作为模块被调用时就是自己的名字
    address = '207 N. Defiance St, Archbold, OH'
    #邮箱地址
    user_agent = 'Foundations of Python Network Programming example search1.py'
    #关于user_agent https://www.jianshu.com/p/c5cf6a1967d1
    location = Nominatim(user_agent=user_agent).geocode(address)
    print(location.latitude, location.longitude)
    #取经纬值
