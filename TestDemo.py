from big_ol_pile_of_manim_imports import *


class Scene_0(Scene):
    def construct(self):

        svgvg = VGroup()
        text0 = TextMobject("想象这里有一千瓶酒")
        svgvg.add(text0)
        # 酒瓶动画
        for i in range(3):
            svgs = VGroup()
            for j in range(20):
                svgs.add(SVGMobject("Resources\\test.svg", color="#38b3e4"))
                svgs[j].set_height(0.8)
            svgs.add(TextMobject("......"))
            svgs.arrange(RIGHT)
            svgvg.add(svgs)
        svgvg.add(TextMobject("......"))
        svgvg.arrange(BOTTOM)
        self.play(ShowCreation(svgvg))
        self.wait()
        # 第二句话
        text1 = TextMobject("但是其中两瓶被人下了毒(毒药1个小时起效)")
        text1.align_to(text0, TOP)
        self.play(Transform(text0, text1))
        self.wait()
        # 酒瓶变色
        self.play(FadeToColor(svgvg[1][3], RED), FadeToColor(svgvg[2][5], RED))
        self.wait()
        # 第三句话
        self.remove(text0)
        svgvg.remove(text0)
        text0 = TextMobject("你有20只老鼠，如何在1小时内找出两瓶毒酒呢?")
        text0.align_to(text1, TOP)
        self.play(Transform(text1, text0))
        self.wait(5)
        # 第四句话
        self.remove(text1)
        text1 = TextMobject("这似乎不可能，但是只要再增加一个条件")
        text1.align_to(text0, TOP)
        self.play(Transform(text0, text1))
        self.wait()
        # 结束
        self.remove(text0)
        self.play(FadeOut(text1), FadeOut(svgvg))
        self.remove(text1, svgvg)


class Scene_1(Scene):
    def construct(self):
        vg = VGroup()
        text0 = TextMobject("每瓶酒都拥有自己的编号，从0开始")

        hg0 = VGroup()
        hg0.add(SVGMobject("Resources\\test.svg", color="#38b3e4"),
                SVGMobject("Resources\\test.svg", color="#38b3e4"),
                SVGMobject("Resources\\test.svg", color="#38b3e4"),
                SVGMobject("Resources\\test.svg", color="#38b3e4"),
                SVGMobject("Resources\\test.svg", color="#38b3e4"),
                SVGMobject("Resources\\test.svg", color="#38b3e4"),
                SVGMobject("Resources\\test.svg", color="#38b3e4"),
                SVGMobject("Resources\\test.svg", color="#38b3e4"))
        hg0.arrange(RIGHT, buff=0.8)

        hg1 = VGroup()
        hg1.add(TextMobject("0"), TextMobject("1"), TextMobject("2"),
                TextMobject("3"), TextMobject("4"), TextMobject("5"),
                TextMobject("6"), TextMobject("7"))
        for i in range(8):
            hg1[i].align_to(hg0[i], UR)

        hg2 = VGroup()
        for i in range(8):
            t = TextMobject(bin(i)[2:].zfill(3))
            hg2.add(t)
            t.align_to(hg1[i], UR)
        vg.add(text0)
        vg.add(hg0)
        vg.add(hg1)
        vg.add(hg2)
        vg.arrange(BOTTOM)
        self.play(Write(text0))
        self.play(ShowCreation(hg0))
        self.play(Write(hg1))
        self.wait()

        text1 = TextMobject("将这些编号用二进制表示")
        text1.align_to(text0, TOP)
        self.play(Transform(text0, text1))
        self.wait()
        self.play(Transform(hg1.copy(), hg2))

        self.remove(text0)
        text0 = TextMobject("如果只有1瓶毒酒，那么这是一个经典的问题")
        text0.align_to(text1, TOP)
        self.play(Transform(text1, text0))
        self.wait(2)

        self.remove(text1)
        text1 = TextMobject("大家都知道10只老鼠找出1000瓶中的1瓶毒酒的方法")
        text1.align_to(text0, TOP)
        self.play(Transform(text0, text1))
        self.wait(2)

        self.remove(text0)
        text0 = TextMobject("这个方法的精髓就在于利用了2进制")
        text0.align_to(text1, TOP)
        self.play(Transform(text1, text0))
        self.wait(2)

        self.remove(text1)
        text1 = TextMobject("但是仅仅靠这个，是不能解决今天的问题的")
        text1.align_to(text0, TOP)
        self.play(Transform(text0, text1))
        self.wait(2)

        l0 = Line(UL, DR, color=RED)
        l1 = Line(UR, DL, color=RED)
        self.play(Write(l0), Write(l1))
        self.wait(2)

        self.remove(text0)
        text0 = TextMobject("那么假如我们还知道，两瓶毒酒的编号的差呢？")
        text0.align_to(text1, TOP)
        self.play(Transform(text1, text0))
        self.play(FadeOutAndShiftDown(l0), FadeOutAndShiftDown(l1))
        self.wait(5)


class Scene_2(Scene):
    def construct(self):
        text0 = TextMobject("事实上，如果知道两瓶毒酒编号的差，就可以成功找出它们")
        text0.shift(TOP + DOWN)
        self.play(Write(text0))
        self.wait(2)

        text1 = TextMobject("你不过只是再需要知道两瓶毒酒编号的和就可以了")
        text1.align_to(text0, TOP)
        self.play(Transform(text0, text1))
        self.wait(2)

        mt0 = TexMobject(r"\begin{cases}A-B=S\\A+B=???\\\end{cases}")
        self.play(FadeInFromDown(mt0))
        self.wait(3)

        self.remove(text0)
        text0 = TextMobject("所以接下来的主要任务，就是想办法得到这个和")
        text0.align_to(text1, TOP)
        self.play(Transform(text1, text0))
        self.wait(2)

        self.remove(text1)
        text1 = TextMobject("你能想到方法吗？")
        text1.align_to(text0, TOP)
        self.play(Transform(text0, text1))
        self.wait(5)

        self.play(FadeOut(text0), FadeOut(text1), FadeOut(mt0))
        self.wait()


class Scene_3(Scene):
    def construct(self):
        text0 = TextMobject("我们依然可以试试故技重施(使用仅1瓶毒酒的方法)")
        text0.shift(TOP + DOWN)
        text1 = TextMobject("让第1只老鼠喝所有编号(2进制)的第1位为1的酒")
        text2 = TextMobject("让第2只老鼠喝所有编号的第2位为1的酒")
        text3 = TextMobject("以此类推，10只老鼠其实可以喝1024瓶酒")
        vg0 = VGroup(text0, text1, text2, text3).arrange(BOTTOM)

        self.play(Write(text0))
        self.wait(2)
        self.play(Write(text1))
        self.wait(2)
        self.play(Write(text2))
        self.wait(2)
        self.play(Write(text3))
        self.wait(2)
        self.play(FadeOutAndShift(vg0))
        self.wait(2)

        text0 = TextMobject("此时我们可以想一想，1小时后必然会出现死老鼠")
        text0.shift(TOP + DOWN)
        text1 = TextMobject("假设第3只老鼠死亡，这会说明什么呢？")
        text2 = TextMobject("如果毒酒只有1瓶，那说明毒酒的编号第3位为1")
        text3 = TextMobject("如今则说明2瓶毒酒中至少有1瓶的编号第3位为1")
        vg0 = VGroup(text0, text1, text2, text3).arrange(BOTTOM)

        self.play(Write(text0))
        self.wait(2)
        self.play(Write(text1))
        self.wait(5)
        self.play(Write(text2))
        self.wait(2)
        self.play(Write(text3))
        self.wait(2)
        self.play(FadeOutAndShift(vg0))
        self.wait(2)

        text0 = TextMobject("假设2瓶毒酒的编号如下")
        text0.shift(TOP + 0.2 * DOWN)
        text1 = TextMobject("1001101001\\\\1100100100")
        text2 = TextMobject("那么，10老鼠的生死状况就会是这样(0生1死)")
        text3 = TextMobject("1101101101")
        vg0 = VGroup(text0, text1, text2, text3).arrange(BOTTOM)

        self.play(Write(text0))
        self.wait(2)
        self.play(Write(text1))
        self.wait(2)
        self.play(Write(text2))
        self.wait(2)
        self.play(Write(text3))
        self.wait(5)

        t0 = TextMobject("这其实就是一个\\text{Or}操作")
        t0.align_to(text0, TOP)
        t2 = TextMobject("\\text{Or-----------------------------}")
        t2.align_to(text2, TOP)
        self.play(Transform(text0, t0), Transform(text2, t2))
        self.wait(3)
        self.play(FadeOutAndShift(vg0))


class Scene_4(Scene):
    def construct(self):
        text0 = TextMobject("但是这样还是不够，别忘了我们还有另外10只老鼠")
        text0.shift(TOP + DOWN)
        text1 = TextMobject("套路是一样的，但这一次要喝的是编号为0的酒")
        text2 = TextMobject("让第1只老鼠喝所有编号的第1位为0的酒")
        text3 = TextMobject("让第2只老鼠喝所有编号的第2位为0的酒")
        vg0 = VGroup(text0, text1, text2, text3).arrange(BOTTOM)

        self.play(Write(text0))
        self.wait(2)
        self.play(Write(text1))
        self.wait(2)
        self.play(Write(text2))
        self.wait(2)
        self.play(Write(text3))
        self.wait(2)
        self.play(FadeOutAndShift(vg0))
        self.wait(2)

        text0 = TextMobject("还是假设2瓶毒酒的编号如下")
        text0.shift(TOP + 0.2 * DOWN)
        text1 = TextMobject("1001101001\\\\1100100100")
        text2 = TextMobject("那么，10老鼠的生死状况就会是这样(1生0死)")
        text3 = TextMobject("1000100000")
        vg0 = VGroup(text0, text1, text2, text3).arrange(BOTTOM)

        self.play(Write(text0))
        self.wait(2)
        self.play(Write(text1))
        self.wait(2)
        self.play(Write(text2))
        self.wait(2)
        self.play(Write(text3))
        self.wait(5)

        t0 = TextMobject("这其实就是一个\\text{And}操作")
        t0.align_to(text0, TOP)
        t2 = TextMobject("\\text{And-----------------------------}")
        t2.align_to(text2, TOP)
        self.play(Transform(text0, t0), Transform(text2, t2))
        self.wait(3)
        self.play(FadeOutAndShift(vg0))


class Scene_5(Scene):
    def construct(self):
        text0 = TextMobject("至此，20只老鼠献上了最后的信息\\\\我们已经可以知道毒酒的编号了")
        text0.shift(TOP + DOWN)
        text1 = TextMobject("什么？你说你还不知道？")
        text1.next_to(text0, BOTTOM)
        text2 = TextMobject("不要忘了，我们其实只缺A+B的值\\\\而得到它所要做的仅仅是一些简单的计算")
        text2.next_to(text0, BOTTOM)

        self.play(Write(text0))
        self.wait(3)
        self.play(Write(text1))
        self.wait(2)
        self.play(Transform(text1, text2))
        self.wait(2)
        text3 = TexMobject("x=\\text{Or}(A,B)\\\\y=\\text{And}(A,B)")
        text3.shift(DOWN)
        self.play(Write(text3))
        self.wait(2)
        t3 = text3.copy().shift(TOP)
        self.play(FadeOut(text0), FadeOut(text1), FadeOut(text2),
                  Transform(text3, t3))
        self.wait(2)
        text4 = TextMobject("要计算A+B，我们还需要知道的是\\\\$z=\\text{Xor}(A,B)=???$")
        text4.next_to(t3, BOTTOM)
        self.play(Write(text4))
        self.wait(5)
        text5 = TextMobject("\\text{Xor}是指对每一位进行如下的操作\\\\相同的为0，不同的为1")
        text5.next_to(text4, BOTTOM)
        self.play(Write(text5))
        self.wait(2)
        self.play(FadeOut(text3), FadeOut(t3), FadeOut(text4), FadeOut(text5))
        self.wait(2)


class Scene_6(Scene):
    def construct(self):
        text0 = TextMobject("其实不难证明\\\\$z=\\text{Xor}(A,B)=\\text{Xor}(x,y)$")
        text0.shift(TOP + DOWN)
        text1 = TextMobject("对于x和y的某一位，什么情况下它们相同呢？")
        text1.next_to(text0, BOTTOM)
        text2 = TextMobject("x和y某1位上的数同时为1\\\\那么A和B这位必然也同时为1")
        text2.next_to(text0, BOTTOM)
        text3 = TextMobject("x和y某1位上的数同时为0\\\\那么A和B这位必然也同时为0")
        text3.next_to(text2, BOTTOM)

        self.play(Write(text0))
        self.wait(3)
        self.play(Write(text1))
        self.wait(2)
        self.play(Transform(text1, text2))
        self.wait(2)
        self.play(Write(text3))
        self.wait(2)
        self.play(FadeOutAndShift(text0), FadeOutAndShift(text1),
                  FadeOutAndShift(text2), FadeOutAndShift(text3))
        self.wait(2)
        text4 = TextMobject("至此，我们知道了")
        text4.shift(TOP + DOWN)
        self.play(Write(text4))
        self.wait(2)
        tm = TexMobject(r"\begin{cases}S=A-B\\x=\text{Or}(A,B)\\y=\text{And}(A,B)\\z=\text{Xor}(A,B)=\text{Xor}(x,y)\end{cases}")
        self.play(Write(tm))
        self.wait(2)
        tm2 = tm.copy().shift(TOP + 2*DOWN)
        self.play(FadeOutAndShift(text4),Transform(tm,tm2))
        self.wait(2)
        text5 = TextMobject("其实Xor就是不进位的加法，而进位也容易")
        text5.next_to(tm2,BOTTOM)
        self.play(Write(text5))
        self.wait(2)
        text6 = TextMobject("y就是所要进的位，只要加上2y就可以")
        text6.next_to(text5,BOTTOM)
        self.play(Write(text6))
        self.wait(2)
        text7 = TextMobject("那么接下来就只剩最后一步了\\\\$A+B=z+2y$")
        text7.align_to(text5,TOP)
        text8 = TexMobject("A=\\frac{1}{2}(z+2y+S),B=\\frac{1}{2}(z+2y-S)")
        text8.align_to(text6,TOP)
        self.play(Transform(text5,text7),Transform(text6,text8))
        self.wait(20)
        self.play(FadeOutAndShift(tm),FadeOutAndShift(text5),FadeOutAndShift(text6))
        self.wait(10)