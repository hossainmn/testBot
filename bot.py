import discord
from discord.ext import commands

Token = 'NzA0MzUxOTQ5MDA4NDA0NTcz.Xqb5Zg.plT2tlKCu6JhfK6LA8T1GVf0sJk'

bot = commands.Bot(command_prefix='.')
id = bot.get_guild(702478884091723825)
channels = ["commands"]
valid_users = ["MActive#2632", "Hbot#8634"]
bot.remove_command("help")


@bot.event
async def on_ready():
    print('bot is ready')


@bot.command()
async def سلام(ctx):
    await ctx.send("سلام وقتتون بخیر چه کمکی از دستم بر میاد ")


@commands.has_permissions(manage_messages=True)
@bot.command(description="Clears X messages.")
async def clear(ctx, num: int, target: discord.Member = None):
    if num > 500 or num < 0:
        return await ctx.send("Invalid amount. Maximum is 500.")

    def msgcheck(amsg):
        if target:
            return amsg.author.id == target.id
        return True
    deleted = await ctx.channel.purge(limit=num, check=msgcheck)
    await ctx.send(f':thumbsup: Deleted **{len(deleted)}/{num}** possible messages for you.', delete_after=10)


@bot.event
async def on_message(message):

    if message.content == "!help":
        embed = discord.Embed(title="Help on BOT",
                              description=" دسته بندی")

        embed.add_field(name="اقتصادی", value="!1")
        embed.add_field(name="تاریخی", value="!2")
        embed.add_field(name="اندیشه", value="!3")
        embed.add_field(name="روش تحقیق", value="!4")
        embed.add_field(name="متون سیاسی به فارسی", value="!5")
        embed.add_field(name="متون سیاسی به انگلیسی", value="!6")
        embed.add_field(name="روابط بین الملل", value="!7.1 or !7.2")
        embed.add_field(name="جزوه استاد", value="!8")
        embed.add_field(name="جامعه شناسی", value="!9")
        embed.add_field(name="حقوق", value="!10")
        await message.channel.send(content=None, embed=embed)

#!1 اقتصادی
    if message.content == "!1":
        embed = discord.Embed(title="COMMANDS",
                              description="اقتصادی")

        embed.add_field(name="Empty", value=".eg1")
        embed.add_field(name="Empty", value=".eg2")

        await message.channel.send(content=None, embed=embed)

#!2 تاریخی

    if message.content == "!2":
        embed = discord.Embed(title="COMMANDS",
                              description="تاریخی")

        embed.add_field(name="Empty", value=".ta1")
        embed.add_field(name="Empty", value=".ta2")

        await message.channel.send(content=None, embed=embed)


#!3 اندیشه

    if message.content == "!3":
        embed = discord.Embed(title="COMMANDS",
                              description="اندیشه")

        embed.add_field(name="1مکتب فلسفی پوزیتیویسم منطقی", value=".an1")

        await message.channel.send(content=None, embed=embed)

#!4 روش تحقیق

    if message.content == "!4":
        embed = discord.Embed(title="COMMANDS",
                              description="روش تحقیق")

        embed.add_field(name="Empty", value=".rt1")
        embed.add_field(name="Empty", value=".rt2")

        await message.channel.send(content=None, embed=embed)


#!5 متون سیاسی به فارسی
    if message.content == "!5":
        embed = discord.Embed(title="COMMANDS",
                              description=" متون سیاسی به فارسی")

        embed.add_field(name="Empty", value=".msf1")
        embed.add_field(name="Empty", value=".msf2")

        await message.channel.send(content=None, embed=embed)


#!6 متون سیاسی به انگلیسی
    if message.content == "!6":
        embed = discord.Embed(title="COMMANDS",
                              description="متون سیاسی به انگلیسی")

        embed.add_field(name="Empty", value=".mse1")
        embed.add_field(name="Empty", value=".mse2")

        await message.channel.send(content=None, embed=embed)

#!7 روابط بین الملل
    if message.content == "!7.1":
        embed = discord.Embed(title="COMMANDS p1",
                              description=" روابط بین الملل")

        embed.add_field(
            name="ایران و بنیاد گرایی اسلامی در آسیای مرکزی", value=".rb1")
        embed.add_field(
            name="بحران اوکراین و مولفه های نظامی روسیه", value=".rb2")
        embed.add_field(name="تاثیر ظهور داعش بر امنیت ایران", value=".rb3")
        embed.add_field(
            name="تاثیر آزاد سازی اقتصادی بر جامعه قزاقستان", value=".rb4")
        embed.add_field(
            name="تاثیر شخصیتی ناصرالدین شاه بر توسعه نیافتگی", value=".rb5")
        embed.add_field(
            name="تبیین ژئوپولیتیکی ایران و قزاقستان", value=".rb6")
        embed.add_field(name="تحول و نقش تصوف در آسیای مرکزی", value=".rb7")
        embed.add_field(
            name="تغییر و تداوم سیاست خاورمیانه ای روسیه", value=".rb8")
        embed.add_field(
            name="جایگاه داعش در امنیتی شدن سیاست خارجی ایران", value=".rb9")
        embed.add_field(
            name="جهانی شدن و منطقه گرایی نوین در آسیا شرقی", value=".rb10")
        embed.add_field(name="چالش چین و آمریکا بر سر هژمونی ", value=".rb11")
        embed.add_field(
            name="حضور سیاسی و اقتصادی پاکستان در خلیج فارس", value=".rb12")
        embed.add_field(name="دولت اسلامی خلافت خراسان", value=".rb13")
        embed.add_field(
            name="روابط ترکیه و ارمنستان و ایران و ارمنستان", value=".rb14")
        embed.add_field(
            name="زمینه و عوامل توسعه روابط روسیه و حماس", value=".rb15")
        embed.add_field(
            name="سیاست ایرانیان ارمنی در زمان افشاریه", value=".rb16")
        embed.add_field(
            name="شماره_بیست و سوم انتشارات_سیاست نامه", value=".rb17")
        embed.add_field(
            name="عملکرد شورای امنیت در معضل بوسنی و هرزه گوین", value=".rb18")
        embed.add_field(
            name="عوامل توسعه نیافتگی روابط ایران و گرجستان", value=".rb19")
        embed.add_field(name="فصلنامه راهبردی شماره ۷۳", value=".rb20")
        await message.channel.send(content=None, embed=embed)

    if message.content == "!7.2":
        embed = discord.Embed(title="COMMANDS p2",
                              description=" روابط بین الملل")
        embed.add_field(name="کرنوپولیتیک انرژی ایران و ترکیه ", value=".rb21")
        embed.add_field(name="مجله سیاست نامه شماره ۳", value=".rb22")
        embed.add_field(name="مجله گاه نامه شماره ۶", value=".rb23")
        embed.add_field(name="مداخله آمریکا در بحران بوسنی", value=".rb24")
        embed.add_field(
            name="مذاکرات هسته ای و منازعه ایران و امریکا", value=".rb25")
        embed.add_field(
            name="مسئله اکراد بر روابط ترکیه و ایران", value=".rb26")
        embed.add_field(
            name="موانع شکل گیری جامعه مدنی در روسیه", value=".rb27")
        embed.add_field(
            name="مولفه های ژئوپولیتیکی سیاست خارجی روسیه", value=".rb28")
        await message.channel.send(content=None, embed=embed)
 #!8 جزوه استاد
    if message.content == "!8":
        embed = discord.Embed(title="COMMANDS",
                              description="جزوه استاد")

        embed.add_field(name="اندیشه های سیاسی در اسلام و ایران", value=".jo1")
        embed.add_field(
            name="برنامه_درسی_دوره_کارشناسی_علوم_سیاسی", value=".jo2")

        await message.channel.send(content=None, embed=embed)

#!9 جامعه شناسی
    if message.content == "!9":
        embed = discord.Embed(title="Help on BOT",
                              description="جامعه شناسی")

        embed.add_field(name="خود و نهاد", value=".js1")
        embed.add_field(name="ذهن یک محاسبه گر", value=".js2")
        embed.add_field(name="ضمیر ناخودآگاه", value=".js3")

        await message.channel.send(content=None, embed=embed)


#!10 حقوق

    if message.content == "!10":
        embed = discord.Embed(title="Help on BOT",
                              description="حقوق")

        embed.add_field(name="رویارویی جدیدیان و روسیه تزاری", value=".ho1")
        embed.add_field(name="Empty", value=".ho2")

        await message.channel.send(content=None, embed=embed)

    await bot.process_commands(message)

# * 1 اقتصادی  (eg)


# *2 تاریخی  (ta)


# *3 اندیشه (an)
@bot.command()
async def an1(ctx):
    await ctx.send('https://drive.google.com/open?id=1ocWKl0VQg88s5gPhiXUZ8ovKvbD_EZk7')

# *4 روش تحقیق  (rt)


# *5 متون سیاسی به فارسی  (msf)


# *6 متون سیاسی به انگلیسی (mse)


# *7 روابط بین الملل (rb)
@bot.command()
async def rb1(ctx):
    await ctx.send('https://drive.google.com/open?id=1gp28xy7ynO9YLG4vQ4w_QolXVgKY8_06')


@bot.command()
async def rb2(ctx):
    await ctx.send('https://drive.google.com/open?id=1VHNTM2BNeXnPdrnIlU6Ae5S7WFgedk-Y')


@bot.command()
async def rb3(ctx):
    await ctx.send('https://drive.google.com/open?id=1A8XCZ2qDrjRPx9MYJkPpy8rit2rcsng5')


@bot.command()
async def rb4(ctx):
    await ctx.send('https://drive.google.com/open?id=1avnL7H9aF0eeftFbZJaFwsI0D3oCMYiT')


@bot.command()
async def rb5(ctx):
    await ctx.send('https://drive.google.com/open?id=1jlx1pFUb7FYB-5qQUo-QkEgk6wjOCWHR')


@bot.command()
async def rb6(ctx):
    await ctx.send('https://drive.google.com/open?id=1MgfosgeVBMJLHw4pq__Se0qcZKbSnUdi')


@bot.command()
async def rb7(ctx):
    await ctx.send('https://drive.google.com/open?id=1xfiBiSqCGCQ2oK8X1M7VPudJLchyZlqg')


@bot.command()
async def rb8(ctx):
    await ctx.send('https://drive.google.com/open?id=11PcqDDD2Rsu5Gx4hbJmKAUnNjHIfC_5F')


@bot.command()
async def rb9(ctx):
    await ctx.send('https://drive.google.com/open?id=1aKFPD6InOxV4ndit9k5fCoh21V3-Ug1-')


@bot.command()
async def rb10(ctx):
    await ctx.send('https://drive.google.com/open?id=1Ebinc_i9D3x7ZNcVm-JGoiMh6c8lSx-5')


@bot.command()
async def rb11(ctx):
    await ctx.send('https://drive.google.com/open?id=18HqBDwBI6Uz1Plle86MbWuxX-jzbpcBj')


@bot.command()
async def rb12(ctx):
    await ctx.send('https://drive.google.com/open?id=1PrimKy66rvmNvx6MEg6a_g90u9_ksKcW')


@bot.command()
async def rb13(ctx):
    await ctx.send('https://drive.google.com/open?id=1C41O1zO14WMSbqJd4kAxO6wttXVedpS7')


@bot.command()
async def rb14(ctx):
    await ctx.send('https://drive.google.com/open?id=1eTwNPbH8DNRPi4hL-au9NJv9lbeYCEqX')


@bot.command()
async def rb15(ctx):
    await ctx.send('https://drive.google.com/open?id=1fU2TZUrSQuDSUzUf9IDu6W_t46skhMZF')


@bot.command()
async def rb16(ctx):
    await ctx.send('https://drive.google.com/open?id=1d9835GLdLwZ3SgSxPJZTykCcr3q-SQBM')


@bot.command()
async def rb17(ctx):
    await ctx.send('https://drive.google.com/open?id=1zqkKxRrQANMfOJ5k6z7kmBOyEEdmzRen')


@bot.command()
async def rb18(ctx):
    await ctx.send('https://drive.google.com/open?id=1VkSFDh9_CcngDXI6gV36q4FOBHvTCiQp')


@bot.command()
async def rb19(ctx):
    await ctx.send('https://drive.google.com/open?id=1XUzO0Ga97si2W_aOrxeOcX1m26oYLLvP')


@bot.command()
async def rb20(ctx):
    await ctx.send('https://drive.google.com/open?id=1J8f93u1D-zyvFp25JmzGUZixpm_mCfMW')


@bot.command()
async def rb21(ctx):
    await ctx.send('https://drive.google.com/open?id=1VbnNZu5qalWi92WUjOtu0IV1ESefD_VK')


@bot.command()
async def rb22(ctx):
    await ctx.send('https://drive.google.com/open?id=1XSlkMG-68gdq05C32AbU8arE_lgwdib-')


@bot.command()
async def rb23(ctx):
    await ctx.send('https://drive.google.com/open?id=1IvgEX4eqd5TJBa1NRWxLeBdzY0Fu4XlZ')


@bot.command()
async def rb24(ctx):
    await ctx.send('https://drive.google.com/open?id=1HoC4zw-e71gKrZv-fS9SJJPK78Tbv67-')


@bot.command()
async def rb25(ctx):
    await ctx.send('https://drive.google.com/open?id=1svs0eZ3_T35go60K8HwZntwrAzPNvWCk')


@bot.command()
async def rb26(ctx):
    await ctx.send('https://drive.google.com/open?id=1-AhiyQDuzkUgKLRTvk6L8lonbtAUyTDb')


@bot.command()
async def rb27(ctx):
    await ctx.send('https://drive.google.com/open?id=1UIb6HpGWj0rreWzL4aWB0dS_g15bBSe6')


@bot.command()
async def rb28(ctx):
    await ctx.send('https://drive.google.com/open?id=1ymih1NK_cJhpd7ttvvF9G2mp6h8HJK34')


# @bot.command()
# async def rb8(ctx):
#     await ctx.send('')


# *8 جزوه استاد  (jo)
@bot.command()
async def jo1(ctx):
    await ctx.send('https://drive.google.com/open?id=1EydGIHUi82RUdEQyTmvgheEKsYbvMFTX')


@bot.command()
async def jo2(ctx):
    await ctx.send('https://drive.google.com/open?id=1AGT6dFTOtNqkrCltdwlGyrRI2RySls83')

# *9 جامعه شناسی  (js)


@bot.command()
async def js1(ctx):
    await ctx.send('https://drive.google.com/open?id=1NReirLQMt2xyHBCx18HL_Ekw-pxOOfoB')


@bot.command()
async def js2(ctx):
    await ctx.send('https://drive.google.com/open?id=1KU-RjN_SSLWgOyckw4uDlUcaTSCvlP1I')


@bot.command()
async def js3(ctx):
    await ctx.send('https://drive.google.com/open?id=1j6kWvX6WgsUKlIp2v8vZeZzxfmydLb1e')

# *10 حقوق  (ho)
@bot.command()
async def ho1(ctx):
    await ctx.send('https://drive.google.com/open?id=1PZGDG6CsILvgvxh8mIdArvzXtcX-FZGJ')

bot.run(Token)
