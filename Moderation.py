import discord
from discord.ext import commands
from datetime import timedelta

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    #@commands.has_permissions(moderate_members=True)
    async def schedule_public_execution(self, ctx, member: discord.Member, minutes: int):
        duration = timedelta(minutes=minutes)

        # let muted person be the one who Leon called on, or the one who called in if its not Leon
        member_to_mute = ctx.author if ctx.author.id != 694786901181333554 else member
        mention_member = ctx.author.mention if ctx.author.id != 694786901181333554 else member.mention


        await member_to_mute.timeout(
            duration,
            reason=f"Muted by {ctx.author}"
        )

        await ctx.send(f":axe: {mention_member} ordered for public execution in {minutes} minutes.")

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def cancel_public_execution(self, ctx, member: discord.Member):
        await member.timeout(None)

        if ctx.author.id != 694786901181333554:
            self.schedule_public_execution(ctx, member, 10)
            return
        
        await ctx.send(f":flag_white: {member.mention} was pardoned from public execution, hooray:unamused:.")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
