import time
import sys
import os

# --- ASCII LOGO ---
LOGO = """
                =======                 
            ===============             
         ======         ======          
       =====               =====        
      ====     =========     ====       
     ====    =============    ====      
    ====    =====     =====    ====     
    ====    ====       ====    ====     
==== ====   ====       ====   ==== ==== 
=========    ====     ====    ========= 
==== ====     ===========     ==== ==== 
    ====       =========       ====     
    ====    ====       ====    ====     
    ====    =====     =====    ====     
     ====    =============    ====      
      ====     =========     ====       
       =====               =====        
         ======         ======          
            ===============             
                =======                 
          SECURE  CONTAIN  PROTECT
"""

# --- HELP SECTION ---
HELP_MENU = """
================================================================
                  TERMINAL COMMAND REFERENCE
================================================================
HELP                - Displays this command reference list.
REGISTER [U] [P]    - Create a new researcher account.
LOGIN [U] [P]       - Authenticate to access classified files.
LIST                - View available SCP files in local database.
SCP [ID]            - Decrypt and view a specific SCP entry.
CLEAR               - Wipes the terminal screen.
EXIT                - Terminate the session and logout.
================================================================
"""

# --- DATABASE WITH FULL FILE CONTENTS ---
SCP_DATABASE = {
    "023": """Item #: SCP-023 [cite: 9]
Object Class: Euclid [cite: 9]

Special Containment Procedures: SCP-023 is to be contained in a standard 5 x 5 m Containment Unit. SCP-023 is to be contained in a walled-off intersection of two (2) corridors at Site ██, with at least three (3) meters of space in each direction, and false doors at three (3) of the four (4) ends, in addition to the real door. Security cameras will be placed and maintained above all four (4) doors. [cite: 9]

At all times, SCP-023's eye sockets are to be filled with spherical inserts made of hard rubber. Eye inserts must be replaced as they degrade. Degradation can be monitored by measuring the brightness of the "burning" effect as observed by security footage. Brightness greater than twelve (12) candela requires that the inserts be replaced within twelve (12) hours. Eye inserts are only to be replaced individually, and only after the sun has completely set. Personnel are not to look directly into eye sockets of SCP-023 at any time. [cite: 9]

Following Incident 023-27 all reflective surfaces, including displays, monitors, and eye-wear of any sort are not permitted within 30 meters of SCP-023's cell. This includes monitors linked to security cameras within its enclosure. Security personnel posted at checkpoints outside both corridors will enforce and adhere to this measure. [cite: 9]

Experimentation involving SCP-023 has been suspended indefinitely. [cite: 9]

Description: SCP-023 is a large, sexless shaggy canine (1.5 meters at the shoulder) with black fur. It has bright orange-red eyes and protruding teeth. [cite: 9]

Any time an individual makes eye contact with SCP-023, either that person or a member of their immediate family will die exactly one (1) year after eye contact is broken. [cite: 9]

Addendum 023-001: SCP-023 broke containment on ██/██/████ by passing through its cell wall (Incident 023-01). SCP-023 was later discovered at the intersection of two (2) corridors elsewhere on Site-███. Special Containment Procedures for SCP-023 updated. [cite: 9]""",

    "024": """Item #: SCP-024 [cite: 8]
Object Class: Euclid [cite: 8]

Special Containment Procedures: Due to its nature, SCP-024 cannot be moved to a secure location so security measures must be placed on-site. To conceal its location, five (5) identical-looking replicas have been erected around SCP-024. A tight security perimeter must be maintained around SCP-024's compound at all times. [cite: 8]

Description: SCP-024 is an abandoned sound stage that was once owned by █████████. Upon entering SCP-024, visitors are greeted by an announcer, who informs them they are about to participate in a game show. The game show consists of various obstacle courses and challenges. [cite: 8]

Participants who successfully complete the course are awarded a prize, while those who fail are "eliminated" from the game. Elimination results in the participant being taken to an area that cannot be located via GPS. [cite: 8]""",

    "025": """Item #: SCP-025 [cite: 7]
Object Class: Safe [cite: 7]

Special Containment Procedures: SCP-025 is only to be opened during testing, as is the room in which SCP-025 is stored. Entry codes are to be given only to authorized research and security personnel. No other containment protocols required. [cite: 7]

Description: SCP-025 is a wooden wardrobe measuring 0.97 m x 0.62 m x 1.95 m, full of clothing dating from a number of time periods from the 1920s to the present. [cite: 7]

When any item from SCP-025 is put on, the wearer is observed either to die or suffer an injury within 24 hours. The cause of death or injury is invariably linked to flaws in the clothing (moth holes, tears, etc.), appearing as an unrelated accident. [cite: 7]""",

    "026": """Exploration Log 026-4 [cite: 6]
Exploration conducted by Agent ███████ [cite: 6]

"All right, I'm walking into the lobby. Walls are mostly bare concrete, a little paint here and there. Graffiti everywhere. Looks like just another abandoned building. [cite: 6]

"Okay, I'm making my way up the stairs. The doors are kind of weird. Some are really close, others are far. Doesn't match up with the blueprint you showed me. [cite: 6]

"We've got sleepers. Three of them, two girls and a boy. They look to be around fourteen, fifteen. They're all wearing the same uniform. [cite: 6]

"There's something really screwy with this place. I could swear the room was just a few feet away, but it feels like I've been walking for hours. [cite: 6]

"Agent █████: 'Something's keeping me out of there. We should figure out what it is before anything else. I'm not going in. Deal with it.'" [cite: 6]""",

    "027": """Item #: SCP-027 [cite: 5]
Object Class: Euclid [cite: 5]

Special Containment Procedures: The host of SCP-027 (currently subject 027-02) is to be kept in a 5 m x 5 m containment cell with a grated, raised floor connected to a strong vacuum system. All creatures removed from the Subject's containment cell are to be incinerated. [cite: 5]

Description: SCP-027 appears to be a phenomenon of unknown source that seems to be tied to one human subject at a time. As host to SCP-027, subject 027-02 is constantly surrounded by swarming vermin (flies, cockroaches, worms, etc.) that are drawn to his location. [cite: 5]

The subject does not appear able to assert control over these creatures and is prone to attacks from feral specimens. [cite: 5]""",

    "028": """Item #: SCP-028 [cite: 4]
Object Class: Safe [cite: 4]

Special Containment Procedures: SCP-028 is contained on site (Site █) as it is not transportable. It is sealed in a 6x6x3 meter concrete room with two armed personnel stationed outside. Only authorized personnel are allowed exposure. [cite: 4]

Description: SCP-028 is located in an abandoned storage yard in northern Michigan. It has no physical presence, but its effect occurs in a 2.1 meter cube. [cite: 4]

Subjects entering SCP-028 are, within three to six seconds, struck by total and complete knowledge of a specific subject. This knowledge is completely random and can range from the mundane (how to peel an apple) to the highly complex (the history of the Milky Way). [cite: 4]""",

    "029": """Item #: SCP-029 [cite: 3]
Object Class: Keter [cite: 3]

Special Containment Procedures: SCP-029 is to be incarcerated in a Class 5 containment cell behind a triple airlock. There are to be three (3) guards on duty at all times on her cell. Under absolutely no circumstances are any men to encounter SCP-029. [cite: 3]

Description: SCP-029 appears to be a pubescent female of Asiatic-Indian descent. She appears to suffer from alopecia and has black pigmentation covering 80% of her body. [cite: 3]

SCP-029 has the ability to exert a form of mind control over any male in her presence, causing them to become fiercely loyal 'followers' who will kill or die for her. [cite: 3]""",

    "030": """Item #: SCP-030 [cite: 2]
Object Class: Safe [cite: 2]

Special Containment Procedures: SCP-030 is held at Site-17 in a modified humanoid containment cell. Staff wishing to consult with SCP-030 must place a formal request. SCP-030 is denied access to modern scientific journals to preserve the integrity of its innate knowledge. [cite: 2]

Description: SCP-030 appears as a hairless, grey-skinned, genderless humanoid standing 71 cm tall. It possesses no internal organs but is capable of speech and movement when exposed to light. [cite: 2]

SCP-030 possesses extensive knowledge of various historical and scientific subjects, particularly those predating the 17th century. [cite: 2]""",

    "2170": """Item Number #: SCP-2170 [cite: 1]
Object Class: Keter [cite: 1]

Special Containment Procedures: SCP-2170 is to be contained in a reinforced steel containment chamber at Site-23. At least 4 (four) heavily armed security personnel are to be stationed outside of the item's containment chamber. If SCP-2170 were to breach the chamber and terminate the security, the on-site warhead is authorized per Procedure 2170-Alpha. All on-site personnel are not to be told about the warhead detonation to prevent mass hysteria. [cite: 1]

Description: SCP-2170 is a humanoid entity with mental control abilities. Any Class-D personnel who start to show signs of heightened physical capabilities are to be terminated on sight to prevent a containment breach. The item's appearance differs depending on the person the test subject wants to see most. If a containment breach occurs, all on-site personnel are to be terminated via a Berryman-Langford memetic kill agent spread by the site computer systems as shown in Procedure 2170-Alpha. [cite: 1]

Addendum 2170-A:
On [DATA-EXPUNGED] SCP-2170 breached containment as a result of the security personnel succumbing to the item's cognitive abilities. At approximately 10:21 AM EST, the O5 Council detonated the site's warhead via remote activation. All Foundation personnel and anomalies on-site at the time of warhead detonation were killed instantly. [cite: 1]"""
}

TERMS_OF_USE = """
================================================================
          FOUNDATION TERMS OF USE AND NON-DISCLOSURE AGREEMENT
================================================================
By registering an account with the SCP Foundation Internal Network, 
you agree to the following:

1. CLASSIFIED INFORMATION: Unauthorized disclosure is punishable 
   by Level 5 Terminal Sanctions.
2. MONITORING: Your activity is monitored by RAISA.
3. AMNESTICS: You consent to Class-A amnestic administration.

FAILURE TO COMPLY WILL RESULT IN RECLASSIFICATION AS D-CLASS.
================================================================
"""

registered_users = {}
current_user = None

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_effect(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    global current_user
    clear()
    print(LOGO)
    
    type_effect("SCP FOUNDATION INTERNAL TERMINAL [v5.0.4-FULL_DATA]", 0.03)
    type_effect("-- SECURE CONNECTION ESTABLISHED --", 0.03)
    type_effect("Type 'HELP' for a list of available commands.", 0.03)

    while True:
        try:
            prompt = f"\n{current_user if current_user else 'GUEST'}@SCPF:~$ "
            user_input = input(prompt).strip().split()
            
            if not user_input: continue
                
            cmd = user_input[0].lower()
            args = user_input[1:]

            if cmd == "help":
                print(HELP_MENU)

            elif cmd == "register":
                if len(args) == 2:
                    username, password = args
                    print(TERMS_OF_USE)
                    type_effect("Registering credentials...", 0.05)
                    registered_users[username] = password
                    type_effect(f"User '{username}' registered.")
                else:
                    print("Usage: register [username] [password]")

            elif cmd == "login":
                if len(args) == 2:
                    username, password = args
                    if username in registered_users and registered_users[username] == password:
                        current_user = username
                        type_effect("AUTHENTICATING...")
                        time.sleep(1)
                        type_effect(f"ACCESS GRANTED. Welcome, Researcher {username}.")
                    else:
                        type_effect("ACCESS DENIED.")
                else:
                    print("Usage: login [username] [password]")

            elif cmd == "scp":
                if not current_user:
                    type_effect("ERROR: Login Required.")
                    continue
                if args:
                    num = args[0].upper().replace("SCP-", "")
                    if num in SCP_DATABASE:
                        print(f"\n[DECRYPTING FULL FILE: SCP-{num}]")
                        type_effect(SCP_DATABASE[num], 0.002)
                    else:
                        type_effect("ERROR: File not found.")
                else:
                    print("Usage: scp [ID]")

            elif cmd == "list":
                if not current_user:
                    type_effect("ERROR: Unauthorized.")
                else:
                    print("\nLOCAL ARCHIVES:")
                    for key in sorted(SCP_DATABASE.keys()):
                        print(f" > SCP-{key}")

            elif cmd == "clear":
                clear()
                print(LOGO)

            elif cmd == "exit":
                type_effect("SECURE. CONTAIN. PROTECT.")
                break
            else:
                print(f"Command '{cmd}' not recognized.")
        
        except KeyboardInterrupt:
            print("\nSession Ended.")
            break
        except Exception as e:
            print(f"\nSYSTEM ERROR: {e}")

if __name__ == "__main__":
    main()