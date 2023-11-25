import asyncio
import nats

async def main():
    nc = await nats.connect("demo.nats.io")
    js = nc.jetstream()
    sub = await js.pull_subscribe("c.io",stream="cio")
    print("Subscribed to NATS subject. [from subscribe_a]")

    msgs = await sub.fetch()
    msg = msgs[0]
    print(msg)
    await msg.ack()

    await nc.close()

if __name__ == '__main__':
    asyncio.run(main())



