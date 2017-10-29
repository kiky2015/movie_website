# coding=utf-8
import media
import fresh_tomatoes

mm_movie = media.Movie("蒙面唱将","http://image.uczzd.cn/5196554678878746044.jpg?id=0&height=422&width=750&width=500&height=283",
	"http://video.tudou.com/v/XMzExNzc5MjUzNg==.html?spm=a2h28.8313475.c1.dimg6&t=1&recoid=17211062245499926722&itemid=13003523369651790037&seccateId=10275")

xm_movie = media.Movie("小猫剪指甲","http://image.uczzd.cn/8647236035030100603.jpg?id=0&width=500&height=283",
	"http://video.tudou.com/v/XMjg3MDM0MzcxNg==.html?spm=a2h28.8313475.c1.dimg15&t=1&recoid=16098957288506280120&itemid=10811329080324174387&seccateId=10275")

xg_movie = media.Movie("主人给小狗做运动","http://image.uczzd.cn/5679691738189706424.jpg?id=0&width=500&height=283",
	"http://video.tudou.com/v/XMjc1MTgyMTY4MA==.html?spm=a2h28.8313475.c1.dimg14&t=1&recoid=1192847924701340830&itemid=2856613887683789967&seccateId=10275")

mn_movie = media.Movie("美女唱将","http://image.uczzd.cn/4526123499247314338.jpg?id=0&height=422&width=750&width=500&height=283",
	"http://video.tudou.com/v/XMjc4ODA4NDI5Ng==.html?spm=a2h28.8313475.c2.dimg14&t=1&recoid=5536837958667581744&itemid=23905485360707625&seccateId=10270")

zf_movie = media.Movie("三分钟做好饭","http://image.uczzd.cn/2006007326840517039.jpg?id=0&height=422&width=750&width=500&height=283",
	"http://video.tudou.com/v/XMzA2MTA2NTE0NA==.html?spm=a2h28.8313475.c6.dimg4&t=1&recoid=8835234850442670402&itemid=5141146620558463354&seccateId=10273")

tz_movie = media.Movie("要吃桃子吗","http://image.uczzd.cn/11264525488885211737.jpeg?id=0&width=500&height=283",
	"http://video.tudou.com/v/XMjg0NjI4NDIyMA==.html?spm=a2h28.8313475.c6.dimg13&t=1&recoid=10876345946186365002&itemid=15094601184464948808&seccateId=10273")

movies = [mm_movie,xm_movie,xg_movie,mn_movie,zf_movie,tz_movie]
fresh_tomatoes.open_movies_page(movies)
