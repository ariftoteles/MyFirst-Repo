#version 1

print('x')
print('y')

# #bikin commit
# 1. add files to staging areag
# 2. git add . ==> menambhakan semua file
# 3. git add 0a.py ==> menambahkan file tertentu, tapi kalo udah add . ga perlu langkah ini
# 4. git commit -m "Ini commit pertamaku"
# 5. git log ==> cek log

print('a')
print('b')

# CHECKOUT ==> read only ==> git log --oneline ==> copy code lalu git chechkout (copy code tujuan commit) 
# untuk kembali ke checkout master ==>> git checkout master
# REVERT ==> back to past and modif commit, atau menghapus beberapa commit diantara commit
# RESET ==> back to past and stay on there, not comeback to present ==>> git reset (code) DONT TRY THIS !!!

print('kelima')

### membuat branch
# 1. git branch (nama branch)
# 2. masuk ke branch ==> git checkout (nama branch)
# 3. cek di branch mana ==> git branch -a
# 4. cara hapus, balik dulu ke master lalu 
#  