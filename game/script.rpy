define m = Character("Maiko")
define mc = Character("[mc_name]")
image maiko_smile = "images/Maiko/Maiko_Smile.png"

image bg_1:
    "images/bg/bg_1.png"
    fit "cover"

image bg_4:
    "images/bg/bg_4.png"
    fit "cover"

transform charP:
    xalign 1.4
    yalign 1.0

transform z1:
    zoom 0.8

label splashscreen:
    play music "audio/title_theme.mp3" fadein 1.0
    return

label start:
play music "audio/audio_1.mp3" fadein 1.0
scene bg_1
$ mc_name = renpy.input("Masukkan namamu : ", length=25)
$ mc_name = mc_name.strip()
if mc_name == "":
    $ mc_name = "Yuki"
"Mantap Namamu Adalah [mc_name]." 
"Suatu hari [mc_name] lapar dan belum makan."
scene bg_3 with dissolve

mc "Aku laper bet, coba nyari makanan di minimarket ah"
mc "(Ngecek kantong)"
mc "Untung masih ada 3k, gas ke minimarket lah"
scene bg_1 with dissolve
"5 Menit kemudian"
scene bg_2 with dissolve
mc "Beli apa ya...."
mc "Beli Indomie aja deh"
show item_1 at truecenter
mc "Enak nih"
hide item_1 with dissolve
mc "Bayar ke kasir dulu lah"
"(berjalan ke kasir)"
scene bg_4 with dissolve
show maiko_smile at charP, z1 with dissolve
mc "Kak mau bayar"
show expression "images/Maiko/Maiko_Talk.png" as talk at charP, z1
m "Mau bayar pakai apa?"
hide talk
mc "Pake cash aja kak"
show expression "images/Maiko/Maiko_Talk.png" as talk at charP, z1
m "Oke kalo gitu totalnya 3rb mas"
hide talk
"[mc_name] memberi uang"
show expression "images/Maiko/Maiko_Smile2.png" as senyum at charP, z1
m "Terimakasih selamat berbelanja"
mc "Sama-sama"
hide senyum
hide maiko_smile
scene bg_1 with dissolve
mc "GAS MASAK MIE"
"TAMAT BANG"
return