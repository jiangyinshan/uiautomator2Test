import uiautomator2 as u2
from AutoInput import Util


class Keyboard_Key(object):
    """docstring for Keyboard_Key"""

    def __init__(self, deviceName):
        self.deviceName = deviceName
        self.sanxing6 = "5203adddfc7334c1"
        self.yijia7 = "4e62be76"
        self.d = u2.connect_usb(self.deviceName)

        self.sanxing6_a = [0.098, 0.781]
        self.sanxing6_b = [0.598, 0.873]
        self.sanxing6_c = [0.398, 0.882]
        self.sanxing6_d = [0.305, 0.783]
        self.sanxing6_e = [0.251, 0.7]
        self.sanxing6_f = [0.401, 0.779]
        self.sanxing6_g = [0.508, 0.789]
        self.sanxing6_h = [0.622, 0.784]
        self.sanxing6_i = [0.748, 0.697]
        self.sanxing6_j = [0.694, 0.784]
        self.sanxing6_k = [0.799, 0.789]
        self.sanxing6_l = [0.901, 0.783]
        self.sanxing6_m = [0.808, 0.865]
        self.sanxing6_n = [0.706, 0.872]
        self.sanxing6_o = [0.85, 0.69]
        self.sanxing6_p = [0.943, 0.699]
        self.sanxing6_q = [0.047, 0.7]
        self.sanxing6_r = [0.356, 0.699]
        self.sanxing6_s = [0.194, 0.786]
        self.sanxing6_t = [0.452, 0.7]
        self.sanxing6_u = [0.652, 0.697]
        self.sanxing6_v = [0.497, 0.872]
        self.sanxing6_w = [0.155, 0.699]
        self.sanxing6_x = [0.296, 0.868]
        self.sanxing6_y = [0.556, 0.704]
        self.sanxing6_z = [0.197, 0.867]

        self.yijia7_a = [0.094, 0.766]
        self.yijia7_b = [0.602, 0.84]
        self.yijia7_c = [0.397, 0.842]
        self.yijia7_d = [0.299, 0.764]
        self.yijia7_e = [0.255, 0.697]
        self.yijia7_f = [0.397, 0.769]
        self.yijia7_g = [0.514, 0.768]
        self.yijia7_h = [0.605, 0.774]
        self.yijia7_i = [0.755, 0.7]
        self.yijia7_j = [0.704, 0.771]
        self.yijia7_k = [0.802, 0.771]
        self.yijia7_l = [0.89, 0.768]
        self.yijia7_m = [0.799, 0.842]
        self.yijia7_n = [0.7, 0.838]
        self.yijia7_o = [0.85, 0.695]
        self.yijia7_p = [0.952, 0.702]
        self.yijia7_q = [0.051, 0.704]
        self.yijia7_r = [0.354, 0.7]
        self.yijia7_s = [0.204, 0.771]
        self.yijia7_t = [0.456, 0.7]
        self.yijia7_u = [0.645, 0.697]
        self.yijia7_v = [0.51, 0.842]
        self.yijia7_w = [0.153, 0.692]
        self.yijia7_x = [0.291, 0.84]
        self.yijia7_y = [0.543, 0.699]
        self.yijia7_z = [0.193, 0.842]

    def tapWord(self, word):
        word = word.lower()
        """根据deviceName选择对应按键"""
        if self.deviceName == self.sanxing6:
            if word == "a":
                self.d.click(self.sanxing6_a[0], self.sanxing6_a[1])
            elif word == "b":
                self.d.click(self.sanxing6_b[0], self.sanxing6_b[1])
            elif word == "c":
                self.d.click(self.sanxing6_c[0], self.sanxing6_c[1])
            elif word == "d":
                self.d.click(self.sanxing6_d[0], self.sanxing6_d[1])
            elif word == "e":
                self.d.click(self.sanxing6_e[0], self.sanxing6_e[1])
            elif word == "f":
                self.d.click(self.sanxing6_f[0], self.sanxing6_f[1])
            elif word == "g":
                self.d.click(self.sanxing6_g[0], self.sanxing6_g[1])
            elif word == "h":
                self.d.click(self.sanxing6_h[0], self.sanxing6_h[1])
            elif word == "i":
                self.d.click(self.sanxing6_i[0], self.sanxing6_i[1])
            elif word == "j":
                self.d.click(self.sanxing6_j[0], self.sanxing6_j[1])
            elif word == "k":
                self.d.click(self.sanxing6_k[0], self.sanxing6_k[1])
            elif word == "l":
                self.d.click(self.sanxing6_l[0], self.sanxing6_l[1])
            elif word == "m":
                self.d.click(self.sanxing6_m[0], self.sanxing6_m[1])
            elif word == "n":
                self.d.click(self.sanxing6_n[0], self.sanxing6_n[1])
            elif word == "o":
                self.d.click(self.sanxing6_o[0], self.sanxing6_o[1])
            elif word == "p":
                self.d.click(self.sanxing6_p[0], self.sanxing6_p[1])
            elif word == "q":
                self.d.click(self.sanxing6_q[0], self.sanxing6_q[1])
            elif word == "r":
                self.d.click(self.sanxing6_r[0], self.sanxing6_r[1])
            elif word == "s":
                self.d.click(self.sanxing6_s[0], self.sanxing6_s[1])
            elif word == "t":
                self.d.click(self.sanxing6_t[0], self.sanxing6_t[1])
            elif word == "u":
                self.d.click(self.sanxing6_u[0], self.sanxing6_u[1])
            elif word == "v":
                self.d.click(self.sanxing6_v[0], self.sanxing6_v[1])
            elif word == "w":
                self.d.click(self.sanxing6_w[0], self.sanxing6_w[1])
            elif word == "x":
                self.d.click(self.sanxing6_x[0], self.sanxing6_x[1])
            elif word == "y":
                self.d.click(self.sanxing6_y[0], self.sanxing6_y[1])
            elif word == "z":
                self.d.click(self.sanxing6_z[0], self.sanxing6_z[1])

        elif self.deviceName == self.yijia7:
            if word == "a":
                self.d.click(self.yijia7_a[0], self.yijia7_a[1])
            elif word == "b":
                self.d.click(self.yijia7_b[0], self.yijia7_b[1])
            elif word == "c":
                self.d.click(self.yijia7_c[0], self.yijia7_c[1])
            elif word == "d":
                self.d.click(self.yijia7_d[0], self.yijia7_d[1])
            elif word == "e":
                self.d.click(self.yijia7_e[0], self.yijia7_e[1])
            elif word == "f":
                self.d.click(self.yijia7_f[0], self.yijia7_f[1])
            elif word == "g":
                self.d.click(self.yijia7_g[0], self.yijia7_g[1])
            elif word == "h":
                self.d.click(self.yijia7_h[0], self.yijia7_h[1])
            elif word == "i":
                self.d.click(self.yijia7_i[0], self.yijia7_i[1])
            elif word == "j":
                self.d.click(self.yijia7_j[0], self.yijia7_j[1])
            elif word == "k":
                self.d.click(self.yijia7_k[0], self.yijia7_k[1])
            elif word == "l":
                self.d.click(self.yijia7_l[0], self.yijia7_l[1])
            elif word == "m":
                self.d.click(self.yijia7_m[0], self.yijia7_m[1])
            elif word == "n":
                self.d.click(self.yijia7_n[0], self.yijia7_n[1])
            elif word == "o":
                self.d.click(self.yijia7_o[0], self.yijia7_o[1])
            elif word == "p":
                self.d.click(self.yijia7_p[0], self.yijia7_p[1])
            elif word == "q":
                self.d.click(self.yijia7_q[0], self.yijia7_q[1])
            elif word == "r":
                self.d.click(self.yijia7_r[0], self.yijia7_r[1])
            elif word == "s":
                self.d.click(self.yijia7_s[0], self.yijia7_s[1])
            elif word == "t":
                self.d.click(self.yijia7_t[0], self.yijia7_t[1])
            elif word == "u":
                self.d.click(self.yijia7_u[0], self.yijia7_u[1])
            elif word == "v":
                self.d.click(self.yijia7_v[0], self.yijia7_v[1])
            elif word == "w":
                self.d.click(self.yijia7_w[0], self.yijia7_w[1])
            elif word == "x":
                self.d.click(self.yijia7_x[0], self.yijia7_x[1])
            elif word == "y":
                self.d.click(self.yijia7_y[0], self.yijia7_y[1])
            elif word == "z":
                self.d.click(self.yijia7_z[0], self.yijia7_z[1])

    def swipePoints(self, points):
        self.d.swipe_points(points)
        pass

    def swipe(self, points):
        self.d.swipe()


if __name__ == '__main__':
    pass
