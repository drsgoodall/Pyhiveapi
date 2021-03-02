"""Constants for Pyhiveapi."""
SYNC_PACKAGE_NAME = "pyhiveapi"
SYNC_PACKAGE_DIR = "/pyhiveapi/"
ASYNC_PACKAGE_NAME = "apyhiveapi"
ASYNC_PACKAGE_DIR = "/apyhiveapi/"
SMS_REQUIRED = "SMS_MFA"


# HTTP return codes.
HTTP_OK = 200
HTTP_CREATED = 201
HTTP_ACCEPTED = 202
HTTP_MOVED_PERMANENTLY = 301
HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_METHOD_NOT_ALLOWED = 405
HTTP_UNPROCESSABLE_ENTITY = 422
HTTP_TOO_MANY_REQUESTS = 429
HTTP_INTERNAL_SERVER_ERROR = 500
HTTP_BAD_GATEWAY = 502
HTTP_SERVICE_UNAVAILABLE = 503


HIVETOHA = {
    "Attribute": {True: "Online", False: "Offline"},
    "Boost": {None: "OFF", False: "OFF"},
    "Heating": {False: "OFF"},
    "Hotwater": {"MANUAL": "ON", None: "OFF", False: "OFF"},
    "Hub": {
        "Status": {True: 1, False: 0},
        "Smoke": {True: 1, False: 0},
        "Dog": {True: 1, False: 0},
        "Glass": {True: 1, False: 0},
    },
    "Light": {"ON": True, "OFF": False},
    "Sensor": {
        "OPEN": True,
        "CLOSED": False,
        True: "Online",
        False: "Offline",
    },
    "Switch": {"ON": True, "OFF": False},
}

HIVE_TYPES = {
    "Hub": ["hub", "sense"],
    "Thermo": ["thermostatui", "trv"],
    "Heating": ["heating", "trvcontrol"],
    "Hotwater": ["hotwater"],
    "Light": ["warmwhitelight", "tuneablelight", "colourtuneablelight"],
    "Sensor": ["motionsensor", "contactsensor"],
    "Switch": ["activeplug"],
}
sensor_commands = {
    "SMOKE_CO": "self.session.hub.hub_smoke(device)",
    "DOG_BARK": "self.session.hub.hub_dog_bark(device)",
    "GLASS_BREAK": "self.session.hub.hub_glass(device)",
    "CurrentTemperature": "self.session.heating.current_temperature(device)",
    "TargetTemperature": "self.session.heating.target_temperature(device)",
    "Heating_State": "self.session.heating.get_state(device)",
    "Heating_Mode": "self.session.heating.get_mode(device)",
    "Heating_Boost": "self.session.heating.boost(device)",
    "Hotwater_State": "self.session.hotwater.get_state(device)",
    "Hotwater_Mode": "self.session.hotwater.get_mode(device)",
    "Hotwater_Boost": "self.session.hotwater.get_boost(device)",
    "Battery": 'self.session.attr.battery(device["device_id"])',
    "Mode": 'self.session.attr.get_mode(device["hiveID"])',
    "Availability": "self.online(device)",
    "Connectivity": "self.online(device)",
}

PRODUCTS = {
    "sense": [
        'add_list("binary_sensor", p, haName="Glass Detection", hiveType="GLASS_BREAK")',
        'add_list("binary_sensor", p, haName="Smoke Detection", hiveType="SMOKE_CO")',
        'add_list("binary_sensor", p, haName="Dog Bark Detection", hiveType="DOG_BARK")',
    ],
    "heating": [
        'add_list("climate", p, temperatureunit=self.data["user"]["temperatureUnit"])',
        'add_list("sensor", p, haName=" Current Temperature", hiveType="CurrentTemperature", custom=True)',
        'add_list("sensor", p, haName=" Target Temperature", hiveType="TargetTemperature", custom=True)',
        'add_list("sensor", p, haName=" State", hiveType="Heating_State", custom=True)',
        'add_list("sensor", p, haName=" Mode", hiveType="Heating_Mode", custom=True)',
        'add_list("sensor", p, haName=" Boost", hiveType="Heating_Boost", custom=True)',
    ],
    "trvcontrol": [
        'add_list("climate", p, temperatureunit=self.data["user"]["temperatureUnit"])',
        'add_list("sensor", p, haName=" Current Temperature", hiveType="CurrentTemperature", custom=True)',
        'add_list("sensor", p, haName=" Target Temperature", hiveType="TargetTemperature", custom=True)',
        'add_list("sensor", p, haName=" State", hiveType="Heating_State", custom=True)',
        'add_list("sensor", p, haName=" Mode", hiveType="Heating_Mode", custom=True)',
        'add_list("sensor", p, haName=" Boost", hiveType="Heating_Boost", custom=True)',
    ],
    "hotwater": [
        'add_list("water_heater", p,)',
        'add_list("sensor", p, haName="Hotwater State", hiveType="Hotwater_State", custom=True)',
        'add_list("sensor", p, haName="Hotwater Mode", hiveType="Hotwater_Mode", custom=True)',
        'add_list("sensor", p, haName="Hotwater Boost", hiveType="Hotwater_Boost", custom=True)',
    ],
    "activeplug": [
        'add_list("switch", p)',
        'add_list("sensor", p, haName=" Mode", hiveType="Mode", custom=True)',
        'add_list("sensor", p, haName=" Availability", hiveType="Availability", custom=True)',
    ],
    "warmwhitelight": [
        'add_list("light", p)',
        'add_list("sensor", p, haName=" Mode", hiveType="Mode", custom=True)',
        'add_list("sensor", p, haName=" Availability", hiveType="Availability", custom=True)',
    ],
    "tuneablelight": [
        'add_list("light", p)',
        'add_list("sensor", p, haName=" Mode", hiveType="Mode", custom=True)',
        'add_list("sensor", p, haName=" Availability", hiveType="Availability", custom=True)',
    ],
    "colourtuneablelight": [
        'add_list("light", p)',
        'add_list("sensor", p, haName=" Mode", hiveType="Mode", custom=True)',
        'add_list("sensor", p, haName=" Availability", hiveType="Availability", custom=True)',
    ],
    "motionsensor": ['add_list("binary_sensor", p)'],
    "contactsensor": ['add_list("binary_sensor", p)'],
}

DEVICES = {
    "thermostatui": [
        'add_list("sensor", d, haName=" Battery Level", hiveType="Battery")',
        'add_list("sensor", d, haName=" Availability", hiveType="Availability", custom=True)',
    ],
    "trv": [
        'add_list("sensor", d, haName=" Battery Level", hiveType="Battery")',
        'add_list("sensor", d, haName=" Availability", hiveType="Availability", custom=True)',
    ],
    "motionsensor": [
        'add_list("sensor", d, haName=" Battery Level", hiveType="Battery")',
        'add_list("sensor", d, haName=" Availability", hiveType="Availability", custom=True)',
    ],
    "contactsensor": [
        'add_list("sensor", d, haName=" Battery Level", hiveType="Battery")',
        'add_list("sensor", d, haName=" Availability", hiveType="Availability", custom=True)',
    ],
    "sense": [
        'add_list("binary_sensor", d, haName="Hive Hub Status", hiveType="Connectivity")',
    ],
    "hub": [
        'add_list("binary_sensor", d, haName="Hive Hub Status", hiveType="Connectivity")',
    ],
}

ACTIONS = (
    'add_list("switch", a, hiveName=a["name"], haName=a["name"], hiveType="action")'
)
