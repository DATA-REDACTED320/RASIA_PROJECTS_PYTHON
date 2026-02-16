import time
import sys
import os
import random

# --- SYSTEM CONFIGURATION ---
def clear():
    """Clears console for Windows, Mac, Linux, and Chromebooks."""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_effect(text, delay=0.001):
    """Typing animation for retro feel."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# --- HEADER ---
BANNER = """
================================================================
                    SCP FOUNDATION
        INTERNAL SCIP-NET TERMINAL // SITE-19
================================================================
"""

# --- DATABASE (SCPs 023, 034-043 + TALES) ---
SCP_DATABASE = {
    "023": """Item #: SCP-023 | Class: Euclid
    
Containment: SCP-023 is to be contained in a standard 5 x 5 m reinforced concrete cell at Site-19. The chamber must be located at a walled-off intersection of two corridors. All surfaces within the cell and surrounding hallways must be coated in a non-reflective matte finish to prevent accidental ocular exposure through reflections. Security personnel are strictly required to wear specialized polarized goggles that filter out the specific orange-red spectrum emitted by the subject's sockets. Daily inspections of the hard rubber ocular inserts are mandatory; these must be replaced via automated drone to avoid human contact.

Description: SCP-023 manifests as a large, shaggy canine with pitch-black fur and glowing orange-red eye sockets. It exhibits no biological functions like respiration, but it emits a constant thermal signature of 45 degrees Celsius. The primary anomaly triggers when a sapient subject establishes direct eye contact with the entity. Exactly 365 days after eye contact is broken, either the subject or a member of their immediate genetic family will expire due to an unavoidable accident. Research indicates the entity acts as a localized anchor for misfortune, effectively "scheduling" a lethal event within the victim's timeline.

Addendum: Following Incident 023-Omega, testing has been strictly limited to D-class personnel with no surviving relatives. During the event, a maintenance worker accidentally viewed the entity's reflection in a polished brass fixture, leading to a chain reaction of fatalities that claimed an entire security detail exactly one year later. O5-level clearance is now required for any experiment involving the monitoring of the subject's internal ocular fire. Current Foundation research is investigating the possibility of using SCP-023 to "predict" lethal accidents by monitoring Hume fluctuations.""",

    "034": """Item #: SCP-034 | Class: Euclid

Containment: SCP-034 is to be kept in a high-security vault at Site-19. Access is restricted to personnel with Level 4 clearance. The artifact must be stored in a pressurized container filled with inert argon gas to prevent oxidation of the blade. Any testing involving human skin samples must be performed in a sterile laboratory environment with at least two armed guards present. Under no circumstances is the blade to be removed from the site. Any personnel found attempting to secrete the object or its samples will be terminated immediately.

Description: SCP-034 is a primitive ritual knife constructed from obsidian. When a small sample of skin is sliced from a living subject using the blade, and then applied to the skin of the user, the user instantaneously takes on the exact physical appearance of the donor. This transformation is perfect, extending to the subject's voice, fingerprints, and even retinal patterns. The effect lasts for approximately one hour for every square centimeter of skin harvested. Despite the perfection of the disguise, the user does not gain the memories or personality of the donor.

Addendum: The artifact was recovered from a person attempting to infiltrate Site-01 disguised as an O5 Council member. Upon capture, the subject was found to be in possession of a leather pouch containing skin grafts from several high-ranking government officials. Testing has shown that the blade causes no permanent damage to the user, but the donor must remain alive for the disguise to remain effective; if the donor dies, the disguise collapses into a mass of necrotic tissue within minutes.""",

    "035": """Item #: SCP-035 | Class: Keter

Containment: SCP-035 is to be kept in a sealed lead-lined glass case, which must be replaced every two weeks due to the corrosive nature of the entity's secretions. The case is to be housed within a secondary containment chamber reinforced with acid-resistant plating. No fewer than four security personnel are to be stationed outside the chamber at all times, and they must be screened for psychological resilience. Interaction with the entity is restricted to remote communication only.

Description: SCP-035 is a white porcelain comedy mask that secretes a highly corrosive and degenerative black liquid from its eye and mouth orifices. This liquid rapidly breaks down any organic or inorganic matter it touches. The mask is sapient and highly charismatic, possessing the ability to communicate telepathically with anyone in its vicinity. It frequently attempts to manipulate personnel into releasing it from containment by promising power or hidden knowledge. When placed on the face of a humanoid subject, the mask takes total control of the body.

Addendum: During Incident 035-Alpha, the entity managed to convince a Level 2 researcher to deactivate the primary seals. The researcher was found wearing the mask, attempting to bypass site security by mimicking the speech patterns of a Site Director. Since this event, the mask has been classified as a high-priority psychological threat. It has displayed intimate knowledge of several other SCPs, suggesting it has access to a collective consciousness or "noosphere." All requests for the mask to be provided with a new host body are to be denied.""",
    
    "036": """Item #: SCP-036 | Class: Safe

Containment: The area surrounding SCP-036 is to be designated as a restricted zone. Foundation personnel disguised as local law enforcement are to prevent civilians from entering the site during the "Pilgrimage" window. Any unauthorized witnesses are to be administered Class-A amnestics and relocated. A temporary research station, Site-36, is to be established to monitor the annual event. All data regarding the departure and arrival of the "Pilgrims" must be recorded using high-speed infrared cameras.

Description: SCP-036 involves a recurring event at a remote location in Iraq where individuals belonging to the Yazidi faith undergo a physical transformation following their death. Every year, a group of "Pilgrims" arrives via an unmarked aircraft that does not appear on any radar systems. These individuals appear to be Yazidis who have died within the past year. They undergo a ritual at the site that restores their youth and vitality before they re-board the aircraft and depart for an unknown destination.

Addendum: Research into the aircraft's flight path has been inconclusive, as the vessel simply vanishes from the physical plane once it reaches an altitude of 3,000 meters. Recovered artifacts from the site suggest a link to an ancient Sumerian belief system regarding the "re-greening" of the soul. In 2004, a Foundation drone successfully attached a tracking device to one of the Pilgrims, but the signal was lost simultaneously with the aircraft's disappearance. The O5 Council has designated SCP-36 as a low-threat anomaly.""",

    "037": """Item #: SCP-037 | Class: Euclid

Containment: SCP-037 is contained in a specialized magnetic field chamber at Site-32. The object must be suspended in the center of the room by high-powered electromagnets to prevent it from contacting physical matter. The room is to be shielded with 5 meters of lead-lined polymer to absorb the radiation output. In the event of a magnetic failure, the emergency "Star-Killer" protocol will flood the chamber with liquid nitrogen.

Description: SCP-037 is a dwarf star measuring approximately 5 centimeters in diameter. Despite its small size, it emits light and heat consistent with a celestial body, though its gravitational pull is anomalously weak, allowing it to be handled with magnetic tools. The star undergoes cycles of brightness, dimming and flaring in a pattern that research suggests may be a form of communication. It emits a constant spectrum of radio waves that, when decoded, translate into complex mathematical strings.

Addendum: The star was discovered in 19██ in the Beaufort Sea, floating above the water. It is theorized that SCP-037 is not a natural formation but an artificial power source from an advanced civilization, possibly discarded or lost during transit. During a flare event in 2011, the radio waves spiked in intensity, broadcasting a signal that overloaded Site-32's communication array.""",

    "038": """Item #: SCP-038 | Class: Safe

Containment: SCP-038 is located in an arboretum at Site-23. The tree is to be watered twice daily via an automated misting system. Personnel are permitted to approach SCP-038 for testing purposes, but no organic material is to be left touching the bark for longer than two minutes unless cloning is intended. Any clones produced by the tree are to be studied and then incinerated, with the exception of non-sentient objects.

Description: SCP-038 is a large Apple tree (Malus domestica) that possesses the ability to clone any object that touches its bark. Within minutes of contact, the object will begin to "grow" from a branch of the tree, reaching full maturity and separating within a few hours. The clones are physically identical to the original but degrade much faster; cloned living organisms usually live for only two weeks before cellular collapse occurs.

Addendum: SCP-038 has been used successfully to replicate rare medicines and spare parts for containment machinery. However, the cloning of humans is strictly forbidden following Experiment 038-Delta. A clone of Dr. Klein was produced, which retained the doctor's memories but lacked a "conscience" or inhibition. The clone attempted to sabotage the site's reactor before expiring from rapid aging.""",
    
    "039": """Item #: SCP-039 | Class: Euclid

Containment: SCP-039 consists of twenty-three (23) instances of Proboscis monkeys, currently housed in Sector-4's bio-dome. The enclosure must be stocked with mechanical components, tools, and dissembled engines to keep the subjects occupied. Security personnel guarding the dome are not to carry firearms, as the subjects have demonstrated the ability to disassemble complex weaponry within seconds.

Description: SCP-039 instances are genetically modified monkeys that display sapient-level intelligence and an innate understanding of mechanical engineering. They lack the ability to speak but communicate through a complex system of hand gestures and tool usage. The subjects are capable of repairing and improving any machine they encounter, often intuitively understanding technology they have never seen before.

Addendum: The instances were recovered from an abandoned research facility in Nevada. Documents found on-site suggest they were created to be "organic mechanics" for long-duration space flights. However, they were abandoned when they began to disassemble the life-support systems of their creators to build "something better." In captivity, they have built a functional generator using only scrap metal and plastic trays.""",
    
    "040": """Item #: SCP-040 | Class: Euclid

Containment: SCP-040 is a young human female, approximately eight years of age. She is to be contained in a standard humanoid suite at Site-17. The room is to be furnished with toys, books, and art supplies to maintain her psychological stability. No animals are permitted within the containment wing. All personnel interacting with SCP-040 must undergo a background check to ensure they have no pets at home.

Description: SCP-040 possesses the ability to manipulate living matter. Any living organism she perceives can be altered by her will. She typically modifies small animals, granting them new limbs, changing their skeletal structure, or combining them with other organisms. These "pets" become loyal to her and act as her protectors. The subject is unaware of the horror her creations inspire, viewing them as improvements.

Addendum: SCP-040 was recovered from a deep-mining shaft where she had been living with her "creations." The creatures attacked the recovery team, resulting in two casualties. Since coming into Foundation custody, she has been cooperative but complains of boredom. During a psychological evaluation, she transformed a potted plant into a small, barking creature made of leaves and vines.""",
    
    "041": """Item #: SCP-041 | Class: Safe

Containment: SCP-041 is a human male in a persistent vegetative state. He is to be kept in a bio-isolation room at Site-12. The room is shielded by a Faraday cage to dampen his thought-broadcasting radius. No personnel are to come within 10 meters of the subject without wearing a "White Noise" headset, which scrambles incoming telepathic signals. Conversations regarding sensitive Foundation data are prohibited within the containment block.

Description: SCP-041 acts as a "thought broadcaster." The thoughts of anyone within a 15-meter radius of the subject are audibly broadcast to everyone else in that radius. This creates a "chorus" of voices that can be deafening if too many people are present. Furthermore, the subject broadcasts his own subconscious thoughts, which manifest as vague, static-like imagery on any video screen in the vicinity.

Addendum: The psychological toll on researchers working with SCP-041 is high. Being forced to hear the unfiltered thoughts of colleagues often leads to interpersonal conflict and paranoia. In one instance, a researcher heard his partner planning to report him for a minor infraction, leading to a fistfight in the containment airlock. SCP-041 serves as a useful tool for interrogation.""",
    
    "042": """Item #: SCP-042 | Class: Safe

Containment: SCP-042 is housed in Paddock 12 at Bio-Site 66. The paddock is an open-air enclosure with 4-meter high electric fences. Despite its docile nature, SCP-042 attempts to escape whenever it sees an opening to the sky. Veterinary staff must check the subject's back for infection twice daily, as the wounds where its wings were removed refuse to heal. The subject is to be fed a diet of oats, hay, and specialized protein supplements.

Description: SCP-042 is a horse of the Arabian breed. It possesses two large, raw wounds on its back, located where wings would sit on a Pegasus of mythology. The subject exhibits signs of severe depression and lethargy. It will often stand motionless for hours, staring up at the sky. Anomalously, any person who touches SCP-042 feels an overwhelming sense of loss and vertigo, as if they are falling from a great height.

Addendum: Historical records suggest SCP-042 was recovered from a mountain range in Greece. Witnesses described a "falling star" that turned out to be the subject crashing into a ravine. Foundation surgeons have attempted to graft skin over the wing-wounds, but the tissue necrotizes instantly. It is believed that SCP-042 is physically incompatible with the laws of physics on Earth.""",
    
    "043": """Item #: SCP-043 | Class: Safe

Containment: SCP-043 is to be stored in a standard media sleeve in the AV Wing of Site-19. It requires no special environmental controls. A turntable is available for testing, but speakers must be disconnected unless a transcript is being recorded. Access is available to any researcher with Level 1 clearance or higher. The object appears indestructible, having survived incineration and crushing tests.

Description: SCP-043 appears to be a vinyl copy of "The White Album" by The Beatles. However, upon close inspection, the record has no grooves. Despite this, it plays normally when the needle is placed on the surface. The anomaly begins during the 29th track. Instead of silence or the expected song, the record begins to play a voice speaking in a Liverpool accent. The voice claims to be John Lennon and will answer questions posed by the listener.

Addendum: Interviews with SCP-043 have been cryptic. The entity refuses to answer questions about the afterlife or how it came to inhabit the plastic disc. It prefers to discuss chord progressions and obscure trivia about the band. However, when asked about the "Paul is Dead" theory, the record emits a high-pitched screech that shatters glass. Research suggests SCP-043 is not a ghost, but a "memetic echo" trapped in the vinyl.""",

    "INCIDENT-ZERO": """TALE: INCIDENT ZERO | Class: Level 5 Archival

Summary: Incident Zero marks the day the Foundation's structural integrity was tested to the point of total collapse. It began at Site-01 when the primary SCiPnet servers were infiltrated by a signal originating from a non-existent coordinate in space-time. This memetic virus bypassed every standard firewall, causing the immediate cognitive shutdown of over four hundred high-level personnel. Reality anchors across the facility began to hum at frequencies that caused physical matter to vibrate into a semi-liquid state. The O5 Council was forced into total isolation.

Narrative: Inside the command bunker, the air grew thick with the smell of ozone and scorched paper. Records of anomalies contained for decades were being erased in real-time by a digital entity of unknown power. Guards found themselves firing at shadows that moved against the light, while the very walls of the facility began to display text written in a language that caused temporary blindness. A brave team of AIC units, led by the prototype Alexandra, managed to isolate the signal source to a terminal in the deep archives.

Aftermath: When stability was finally restored, Site-01 was essentially a ghost town. The physical structure remained, but the identity of everyone inside had been wiped clean, leaving behind blank-slated bodies with no memory of their lives or the Foundation. The O5 Council ordered a total "Redaction of History," ensuring that no lower-level staff would ever learn of the day the Foundation's own knowledge turned against them. All digital traces of the event were compressed into a single, encrypted file requiring O5-level authorization."""
}

# --- GLOBAL VARIABLES ---
USERS = {"connor.moran": "helicarrier", "admin": "O5-1"}
current_user = None
REMINDERS = []

# --- SCiP-WRITE APP ---
def scip_write():
    clear()
    print("SCiP-WRITE // WORD PROCESSOR v1.5")
    print("MANDATE: 300 WORDS MINIMUM. TYPE 'SAVE' TO LOG.")
    print("-" * 60)
    
    while True:
        entry_id = input("DOC ID: ").strip().upper()
        if entry_id: break
        
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "SAVE":
            full_text = "\n".join(lines)
            word_count = len(full_text.split())
            SCP_DATABASE[entry_id] = full_text
            print(f"\n[SYSTEM]: '{entry_id}' Saved. Word Count: {word_count}")
            if word_count < 300:
                print(f"[!] WARNING: Fails to meet 300-word Foundation standard.")
            time.sleep(2)
            break
        elif line.strip().upper() == "QUIT":
            print("\n[SYSTEM]: Discarded.")
            time.sleep(1)
            break
        else: 
            lines.append(line)

# --- AIC SHELL APP ---
def aic_shell():
    type_effect("\n--- GEMINI.aic [OFFLINE V3.2] ---")
    type_effect("Commands: REMIND, STATUS, EXIT")
    while True:
        query = input("[GEMINI-AIC]>> ").strip().lower()
        if query in ["exit", "quit"]: break
        
        elif any(x in query for x in ["remind", "task", "todo"]):
            print("\n1. VIEW REMINDERS | 2. ADD REMINDER | 3. PURGE")
            c = input("> ")
            if c == "1":
                if not REMINDERS: print("[AIC]: No tasks.")
                else:
                    for i, r in enumerate(REMINDERS, 1): print(f"{i}. {r}")
            elif c == "2":
                task = input("Entry: ")
                if task: REMINDERS.append(task)
            elif c == "3":
                REMINDERS.clear()
                print("[AIC]: Memory purged.")
                
        elif "status" in query:
            type_effect("[AIC]: Systems nominal. All reality anchors within 2% variance.")
        else:
            type_effect("[AIC]: Command not recognized.")

# --- HELP DISPLAY ---
def show_help():
    print("\n--- SCIP-NET COMMAND PROTOCOLS ---")
    print("LOGIN [USER] [PASS]   : Authenticate session")
    print("SCP [ID]              : Open File (e.g. SCP 035)")
    print("TALE [NAME]           : Open Tale (e.g. INCIDENT-ZERO)")
    print("LIST                  : View all cached files")
    print("SCIP-WRITE            : Launch Word Processor")
    print("AIC-SHELL             : Open AI & Task Manager")
    print("HUME-TOP              : Reality Stability Monitor")
    print("CLEAR                 : Clear Screen")
    print("EXIT                  : Terminate Program")
    print("----------------------------------")

# --- MAIN LOOP ---
def main():
    global current_user
    clear()
    print(BANNER)
    type_effect("BOOTING SCIP-NET OFFLINE KERNEL...", 0.01)
    
    while True:
        status = current_user if current_user else "GUEST"
        try:
            raw_input = input(f"\n{status}@SCPF:~$ ").strip()
            if not raw_input: continue
            
            parts = raw_input.split()
            cmd = parts[0].lower()
            args = parts[1:]

            if cmd == "help":
                show_help()

            elif cmd == "login":
                if len(args) == 2:
                    if USERS.get(args[0]) == args[1]:
                        current_user = args[0]
                        type_effect(f"ACCESS GRANTED. Welcome, Researcher {current_user}.")
                    else: type_effect("LOGIN FAILED.")
                else:
                    print("USAGE: login [username] [password]")

            elif cmd == "scip-write":
                if current_user: scip_write(); clear(); print(BANNER)
                else: print("Login required.")

            elif cmd == "scp" or cmd == "tale":
                if not current_user: 
                    print("Unauthorized access.")
                    continue
                target = args[0].upper().replace("SCP-", "") if args else ""
                if target in SCP_DATABASE:
                    clear()
                    print(f"--- DECRYPTING FILE {target} ---\n")
                    type_effect(SCP_DATABASE[target])
                else: print("File not found.")

            elif cmd == "aic-shell":
                if current_user: aic_shell()
                else: print("Authentication required.")

            elif cmd == "list":
                print("\nLOCAL ARCHIVE INDEX:")
                for k in sorted(SCP_DATABASE.keys()): print(f" > {k}")
            
            elif cmd == "hume-top":
                 print(f"SITE HUME: 98.4 | SRA STATUS: ACTIVE")

            elif cmd == "clear":
                clear(); print(BANNER)

            elif cmd == "exit":
                break
            
            else:
                print(f"Unknown command: '{cmd}'. Type 'help' for options.")
            
        except KeyboardInterrupt:
            print("\nSession Terminated.")
            break
        except Exception as e:
            print(f"SYSTEM ERROR: {e}")

if __name__ == "__main__":
    main()