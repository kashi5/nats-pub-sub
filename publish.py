import asyncio
import nats

async def main():
    nc = await nats.connect("demo.nats.io")
    js = nc.jetstream()
    await js.add_stream(name='cio', subjects=['c.io'])

    ack = await js.publish('c.io', b'Hello 13!')
    print(f'Ack: stream={ack.stream}, sequence={ack.seq}')
    # Ack: stream=hello, sequence=1
    await nc.close()

if __name__ == '__main__':
    asyncio.run(main())