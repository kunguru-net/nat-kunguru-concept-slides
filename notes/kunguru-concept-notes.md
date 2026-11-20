
# Kunguru Concept Slides

## Four Levels of Control

### Big Tech Product: Microsoft OneDrive, Gmail, Claude Agent Mode, etc.

Using a big tech product is like living in a college dorm.

- There are rules about what you can do.
- If you break the rules, even inadvertently, you may get kicked out.
- If you get kicked out, that's a big problem - nobody else provides dorms
for this college.
- You're being watched most of the time. There's definitely a record of when
you card into the door, and there are people who can easily get it.
- Advantage: If the toilet clogs, there's a maintenance person.
- Maybe Advantage: You've got a non-optional meal plan.

### Managed Commodity Product: Managed NextCloud, Fastmail, Hermes from a VPS Provider

Using a managed service is more like a long-stay hotel.

- There are still rules.
- Advantage: If you get kicked out and have backups, you can reasonably just
drop in your existing setup with another basically similar provider.
- You're still being watched most of the time, and there's still card scan
records for all the doors.
- Advantage: If the toilet clogs, there's a maintenance person.

### Unmanaged commodity server rental (physical or virtual)

Using unmanaged hosting is like renting an apartment.

- The rules tend to be limited to risks to the provider / other tenants.
- If you have backups you can drop them straight in to any other provider.
- Disadvantage: Routine toilet clogs or dead light bulbs are your problem. Any
software issues are your problem.
- Advantage: If heat fails, you can call the landlord.
- The landlord *can* enter and inspect your apartment, typically with
restrictions.

### Self-hosted

Having a server in our own home / business means you fully own it, like owning
a house.

- Nobody can enforce rules beyond the actual laws. You have full freedom of
speech, freedom of association, and searches require a warrant.
- If it breaks, you fix it yourself or hire the professional of your choice.
- Disadvantage: You need to provide connectivity yourself.

## Core Concept: AI Assistant

Kunguru provides AI assistants for individuals, teams, and groups.

We entirely avoid big-tech lock in, and can support a range of different
configurations depending on user needs.

An AI assistant is a persistent AI agent that you can chat with from any of your
devices, and which can do things for you, including scheduled tasks and
maintaining private or public custom web sites / applications.

We have two different deployment cases to consider:

- A single isolated user
- A team of multiple users who each need their own assistant and will
also be working together.

Related concepts:

- Personalized applications
- Distributed personal presence servers, with the ability for users to move.
  - ex. An activitypub server, XMPP server, or RSS blog provides users with a 
  public identity on a shared server and *should* be portable either with some
  sort of "I have moved" mechanism or an independent identity concept (e.g.
  users have self-signed identity certificates on a DHT or blockchain, although
  identity is hard and cryptographic identity is extra hard in the face of
  non-extreme-expert users).
  - An AI assistant is conceptually portable in this same way, and it's also
  potentially public in a similar way.


## What services

For a minimal AI assistant + custom web apps, this trade-off applies separately 
to three distinct services:

- The agent server. Something like Hermes agent wants a Linux user account
or container.
  - This is the most privacy/autonomy critical component, since it's where user
  data lives persistently.
  - This can easily be on an on-premises physical server (mini PC for 1-4
  users, bigger machine for more). We can probably sell the single user version
  for $100 at least for initial testing.
  - It can also be on a team or multi-tenant cloud server.
- The gateway server. There needs to be something with a public internet
address, and putting that on a local network is hard.
  - This can be a cloud VPS. With the simplest setup, the provider *could*
  snoop traffic but probably won't. It's also possible to set this up so the provider
  can't snoop traffic.
  - If the agent server is in the cloud, this isn't needed.
- The LLM provider. Something needs to generate LLM responses.
  - This can be on premises, but it requires at least $2000 of hardware to be
  useful.
    - Pooling on premises LLM resources across multiple users is really interesting, 
    but kind of complex to set up.
  - This can go to standard cloud APIs
    - If direct from user, provider can see request/response and associate with
      user.
    - If indirect (we resell), then provider can see request/response but
    doesn't directly have end user identity.
    - This can be double-indirect through services like OpenRouter, which will
    also tend to spread requests across multiple providers so no one external 
    provider has your whole history.
  - This can be served through unmanaged cloud resources. This is expensive
  unless shared by many users.
