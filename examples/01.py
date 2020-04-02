import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 01

import destiny
import asyncio

async def main(dest):
    membership = await dest.api.getMembershipFromHardLinkedCredential(76561198063633362)

    mType = membership['membershipType']
    mId = membership['membershipId']

    print(mType, mId)

    profile = await dest.api.getProfile(mType, mId, [destiny.enums.DestinyComponentType.Characters])

    characters = list(profile['characters']['data'].keys())

    await dest.close()


with open('key', 'r') as f:
    dest = destiny.Destiny(f.read())

loop = asyncio.get_event_loop()
loop.run_until_complete(main(dest))
loop.close()

