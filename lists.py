'''
servers_list = ["bngsbl-s-8094","bngsbl-s-8097","bngsbl-s-8103","adh-234","bngsbl-s-8105","bngsbl-s-8108","bngsbl-s-8111","bngsbl-s-8112","bngsbl-s-8113","bngsbl-s-8114","bngsbl-s-8115","bngsbl-s-8116","bngsbl-s-8121","bngsbl-s-8122","bngsbl-s-8123","bngsbl-s-8124"]
new_servers_list = ["abng-123","jre-789","ght-345"]
new_list = servers_list + new_servers_list
print(f"New servers list is: {new_list}")

#print(servers_list)
#print(type(servers_list))

print(servers_list[3])
print(f"Faulty server is: {servers_list[2]}")
servers_list.sort()
print(servers_list)

print(servers_list[0:1])


nums = [10, 20, 30, 40, 50]
nums_squr = []
for num in nums:
    nums_squr.append(num**2)
print(f" squared list is: {nums_squr}")

nums_squred = [num**2 for num in nums]
print(f" squared list is: {nums_squred}")

tv_shows = ["game of thronws", "breaking bad", "the wire", "sherlock", "stranger things"]
tv_shows_upper = []
for shows in tv_shows:
    tv_shows_upper.append(shows.title())

print(f"Tv shows is : {tv_shows_upper}")

tv_show_title = [ show.title() for show in tv_shows if len(show) > 10]

print(f" Tv show title is :{tv_show_title}")


from time import time
start = time()
print([i**2 for i in range(1, 1000000)])
end = time()
print(f"Time taken: {end - start}")


from time import time
start = time()
sqaures = []
for n in range(1, 100000001):
    sqaures.append(n**2)
    end = time()
print(f"Time taken: {end - start}")
'''

nums = range(1, 20)
even_num = []
odd_num = []
for num in nums:
    if num%2 ==0:
        squared = num**2
        if squared >= 4:
            even_num.append(squared)
            even_numa.apenned
    else:
        odd_num.append(num)

print(f"Even numbers are: {even_num}")
print(f"Odd numbers are: {odd_num}")