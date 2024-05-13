


class Physics():
    def __init__(self, p:str, p_working:str, height_p:int ,width:int, max_speed_p:int,stall_speed_p, rotating_index, a_airport, b_airport, laps = 2):
        self.p = p
        self.p_working = p_working
        self.max_speed_p = max_speed_p
        self.height_p = height_p
        self.width_p = width
        self.crashed = False
        self.index = rotating_index
        self.a_airport = a_airport
        self.b_airport = b_airport
        self.laps = laps
        self.stall = stall_speed_p
    def start(self):
        self.window = display.set_mode((700,600))
        self.shpare = Scene("skibidi sigma pomni (digital fortnite chamba flow) xxxtenctation.png", 0, 500,0, 40000, 100)
        self.shparet = Scene("sky.png", 0 ,-19400 ,0, 40000, 20000)
        self.plane = Plane(physics.p, 0,500 - physics.width_p, physics.height_p,physics.width_p, physics.max_speed_p, physics.stall)
        self.a_airport = Scene(physics.a_airport, 0 , 0,0,800,500)
        self.b_airport = Scene(physics.b_airport ,38200 , 0, 0, 800,500)
        self.scene = [shpare,shparet,a_airport, b_airport]
        self.laps_gone = 1
        self.text_surface = font.render(f"Altitude: {shpare.rect.y}", True, (255,255,255))
        self.text_surface2 = font.render(f"Speed: {plane.speed}", True,(255,255,255))
        self.timer = 0
        self.game = True
    def playing(self):
        self.timer += 60/100
        self.text_surface = font.render(f"Altitude: {shpare.rect.y - 500}", True, (255,255,255))
        self.text_surface2 = font.render(f"Speed: {int(plane.speed)}", True, (255,255,255))
        self.text_surface3 = font.render(f"Power: {plane.power}%", True, (255,255,255))
        self.text_surface4 = font.render(f"Left to go: {shpare.rect.x + 39000 + (40000 * (physics.laps - laps_gone))}", True, (255,255,255))
        for e in event.get():
            if e.type == QUIT:
                self.game = False
                self.crashed = True
        self.shparet.reset()
        self.shpare.reset()
        if self.laps_gone < 2:
            self.a_airport.reset()
        if self.shpare.rect.x + 40000 < 100:
            self.laps_gone += 1
            for i in self.scene:
                i.move_forward(-40000)
        print(self.laps == self.laps_gone)
        if self.laps_gone >= self.laps:
            self.b_airport.reset()
        self.window.blit(self.text_surface, (10, 10))
        self.window.blit(self.text_surface2, (10,46))
        self.window.blit(self.text_surface3, (10, 82))
        self.window.blit(self.text_surface4, (450,10))
        
        
        self.plane.reset()


class Scene(sprite.Sprite):
    def __init__(self, image_path, x, y, speed, height, width):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (height, width))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def move_forward(self, px):
        self.rect.x -= px
        
    def move_up(self,px):
        self.rect.y += px

class Plane(sprite.Sprite):
    def __init__(self, image_path, x, y, height, width, max_speed,stall_speed):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (height, width))
        self.original_image = transform.scale(image.load(image_path), (height, width))
        self.rect = self.image.get_rect()
        self.speed = 0
        self.y_speed = 0
        self.x_speed = 0
        self.rect.x = x
        self.rect.y = y
        self.height = height
        self.width = width
        self.angle = 0
        self.engine_working = False
        self.power = 0
        self.max_speed = max_speed
        self.stall_speed = stall_speed

    def toggle_engine(self):
        global timer
        if not self.engine_working and timer > 5:
            self.original_image = transform.scale(image.load(physics.p_working), (self.height, self.width))
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.engine_working = True
            timer = 0
        elif timer > 5:
            self.original_image = transform.scale(image.load(physics.p), (self.height, self.width))
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.engine_working = False
            self.power = 0
            timer = 0
                
    def reset(self):
        
        keys = key.get_pressed()
        if keys[K_w]:
            self.rotate(physics.index * self.speed)
        elif keys[K_s]:
            self.rotate(-(physics.index * self.speed))
        elif keys[K_e]:
            self.toggle_engine()
        elif keys[K_d]:
            if self.power < 100 and self.engine_working:
                self.power += 2
        elif keys[K_a]:
            if self.power > 0:
                self.power -= 2
        elif keys[K_a]:
            if pygame.sprite.collide_rect(self,physics.shpare) and self.speed > 0:
                self.speed -= 0.5
                if self.speed < 0:
                    self.speed = 0
        physics.window.blit(self.image, (self.rect.x, self.rect.y))
        
        if self.speed < self.stall_speed + 1 and not pygame.sprite.collide_rect(self,physics.shpare):
            self.y_speed -= self.stall_speed - self.speed
        if not pygame.sprite.collide_rect(self, physics.shpare):
            if not self.speed < self.stall_speed + 1:
                if self.angle / 90 > 1:
                    self.y_speed = self.max_speed - (self.angle / 90 - 1) * self.speed
                elif self.angle / 90 > 2:
                    self.y_speed = (self.max_speed * 2) - (self.angle / 90 - 2) * self.speed
                else:
                    self.y_speed = (self.angle / 90) * self.speed

        else:
            self.y_speed = 0


        if self.engine_working:
            if self.speed < self.max_speed + 0.1:
                self.speed += 0.3 * self.power / 100
        if self.speed > 0:
            self.speed -= 0.2                                                                                                                                                                                      
        
        if self.angle > 90:
            self.x_speed = 0 - self.speed + self.y_speed
        

        else:
            self.x_speed = self.speed - self.y_speed
        if self.angle > 15:
            if self.speed > 2:
                self.speed -= (self.angle - 40) * 0.01

        for i in physics.scene:
            i.move_forward(self.x_speed)
            i.move_up(self.y_speed)

        
        
    def rotate(self, angle):
        global game

        if not pygame.sprite.collide_rect(self, shpare):
            self.angle += angle
            self.image = pygame.transform.rotate(self.original_image, self.angle)
        else:
            if self.y_speed < -2:
                physics.crashed = True
            else:
                self.angle = 0
                self.image = pygame.transform.rotate(self.original_image, self.angle)
                if self.speed > self.stall_speed:
                    for i in physics.scene:
                        i.move_up(1)
    
                

