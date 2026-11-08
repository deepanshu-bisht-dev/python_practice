import turtle
import random
import math
import time

# --- Screen Setup ---
screen = turtle.Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("#070410")  # Deep festive night sky
screen.title("✨ Shubh Deepawali - Festival of Lights ✨")
screen.tracer(0)  # Turn off auto-refresh for smooth 60 FPS animation

# --- Color Palettes ---
FIREWORK_COLORS = [
    "#FFD700", "#FF4500", "#FF1493", "#00FFFF",
    "#7FFF00", "#FF00FF", "#FFA500", "#FFFFFF", "#FF6347"
]
FAIRY_COLORS = ["#FFD700", "#FF6347", "#00FFFF", "#FF1493", "#7FFF00"]

# --- Draw Static Background Elements (Stars & Greeting) ---
bg_pen = turtle.Turtle()
bg_pen.hideturtle()
bg_pen.penup()

# Draw background stars
for _ in range(90):
    x = random.randint(-480, 480)
    y = random.randint(-100, 330)
    size = random.randint(2, 4)
    bg_pen.goto(x, y)
    bg_pen.dot(size, random.choice(["#FFFFFF", "#FFFACD", "#FFD700"]))

# Draw Festive Greeting Banner
bg_pen.goto(0, 62)
bg_pen.color("#FF4500")
bg_pen.write("✨ SHUBH DEEPAWALI ✨", align="center", font=("Georgia", 36, "bold"))

bg_pen.goto(0, 65)
bg_pen.color("#FFD700")
bg_pen.write("✨ SHUBH DEEPAWALI ✨", align="center", font=("Georgia", 36, "bold"))

bg_pen.goto(0, 20)
bg_pen.color("#FFE4B5")
bg_pen.write("May the Divine Light of Diyas Guide Your Journey from Darkness to Light", 
             align="center", font=("Arial", 14, "italic"))

# --- Draw Diyas Along the Bottom ---
diya_positions = [-360, -180, 0, 180, 360]

def draw_diya_bases():
    for x in diya_positions:
        y = -260
        # Outer golden rim glow
        bg_pen.goto(x - 45, y)
        bg_pen.color("#B8860B", "#8B2500")
        bg_pen.begin_fill()
        bg_pen.setheading(-60)
        bg_pen.circle(52, 120)
        bg_pen.goto(x - 45, y)
        bg_pen.end_fill()

        # Decorative gold border on Diya
        bg_pen.goto(x - 43, y - 3)
        bg_pen.pensize(3)
        bg_pen.color("#FFD700")
        bg_pen.pendown()
        bg_pen.setheading(0)
        bg_pen.forward(86)
        bg_pen.penup()
        bg_pen.pensize(1)

draw_diya_bases()

# --- Dynamic Elements: Flickering Flames & Fairy Lights ---
flame_pen = turtle.Turtle()
flame_pen.hideturtle()
flame_pen.penup()

fairy_pen = turtle.Turtle()
fairy_pen.hideturtle()
fairy_pen.penup()

def update_flames_and_lights(tick):
    flame_pen.clear()
    # Flickering Diya Flames
    for x in diya_positions:
        y = -255
        # Soft Aura Glow
        aura_size = random.randint(36, 44)
        flame_pen.goto(x, y + 15)
        flame_pen.dot(aura_size, "#331A00")
        
        # Outer Orange Flame
        flame_pen.goto(x, y + 14)
        flame_pen.dot(random.randint(22, 27), "#FF4500")
        
        # Middle Gold Flame
        flame_pen.goto(x, y + 12)
        flame_pen.dot(random.randint(14, 18), "#FFA500")
        
        # Inner Bright Core
        flame_pen.goto(x, y + 10)
        flame_pen.dot(random.randint(7, 10), "#FFFFE0")

    # Top Hanging Fairy String Lights
    fairy_pen.clear()
    for i, x in enumerate(range(-480, 500, 30)):
        # Sagging garland curve using cosine
        y = 325 - int(20 * abs(math.sin(x * 0.015)))
        color = FAIRY_COLORS[(i + tick) % len(FAIRY_COLORS)]
        fairy_pen.goto(x, y)
        fairy_pen.dot(9, color)

# --- Firework Particle System ---
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2.0, 9.5)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.color = color
        self.age = 0
        self.lifespan = random.randint(25, 48)
        self.size = random.randint(3, 6)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy -= 0.18  # Gravity pull
        self.vx *= 0.97  # Air drag
        self.age += 1

class FireworkRocket:
    def __init__(self, target_x=None, target_y=None):
        self.x = target_x if target_x is not None else random.randint(-420, 420)
        self.y = -250
        self.target_y = target_y if target_y is not None else random.randint(50, 270)
        self.color = random.choice(FIREWORK_COLORS)
        self.vy = random.uniform(9.0, 13.0)
        self.exploded = False

    def update(self):
        self.y += self.vy
        if self.y >= self.target_y:
            self.exploded = True

fw_pen = turtle.Turtle()
fw_pen.hideturtle()
fw_pen.penup()

rockets = []
particles = []

def spawn_explosion(x, y, main_color):
    second_color = random.choice(FIREWORK_COLORS)
    for i in range(45):
        c = main_color if i % 2 == 0 else second_color
        particles.append(Particle(x, y, c))

# Click anywhere on screen to launch a custom firework!
def on_screen_click(x, y):
    r = FireworkRocket(target_x=x, target_y=max(y, -50))
    rockets.append(r)

screen.onclick(on_screen_click)

# --- Main Animation Loop ---
tick = 0
try:
    while True:
        fw_pen.clear()

        # Randomly launch new rockets
        if random.random() < 0.08 and len(rockets) < 5:
            rockets.append(FireworkRocket())

        # Update & Draw Rising Rockets
        for r in rockets[:]:
            r.update()
            fw_pen.goto(r.x, r.y)
            fw_pen.dot(6, r.color)
            # Rocket trail spark
            fw_pen.goto(r.x, r.y - 8)
            fw_pen.dot(4, "#FFA500")
            if r.exploded:
                spawn_explosion(r.x, r.y, r.color)
                rockets.remove(r)

        # Update & Draw Exploding Particles
        for p in particles[:]:
            p.update()
            if p.age >= p.lifespan:
                particles.remove(p)
            else:
                fw_pen.goto(p.x, p.y)
                current_size = max(1, int(p.size * (1 - p.age / p.lifespan)))
                fw_pen.dot(current_size, p.color)

        # Update Diya flames & fairy lights every 2 frames
        if tick % 2 == 0:
            update_flames_and_lights(tick // 4)

        screen.update()
        tick += 1
        time.sleep(0.02)

except turtle.Terminator:
    pass