import asyncio
import nats

async def main():
    nc = await nats.connect("demo.nats.io")
    js = nc.jetstream()

    try:
        # Create pull-based consumer on 'cio'.
        psub = await js.pull_subscribe("c.io", stream="cio")
        print("Subscribed to NATS subject. [from subscribe_b]")

        while True:
            try:
                # Fetch and ack messages from consumer.
                msgs = await psub.fetch(1000, timeout=1)
                for msg in msgs:
                    await msg.ack()
                    print(f"Received message from consumer d: {msg.data.decode()}")
            except nats.errors.TimeoutError:
                # No new messages, handle timeout if needed
                pass
            except Exception as e:
                print(f"Error fetching and processing messages: {e}")
                # Optionally, you can re-subscribe in case of an error
                psub = await js.pull_subscribe("c.io", stream="cio")

    except Exception as e:
        print(f"Error in NATS subscription: {e}")

if __name__ == '__main__':
    asyncio.run(main())
