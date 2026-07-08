# AI Assistant Bot Specification

## Goal

Telegram bot for AI chat with user profiles, message history, admin tools and future subscription system.

## Core Features

### User
- Register user on /start
- Store user in SQLite
- Show user profile
- Store language
- Store AI message count

### AI Chat
- Enable AI mode
- Disable AI mode
- Save user messages
- Save assistant messages
- Clear chat history
- Prepare context for OpenAI
- Temporary test AI response

### Admin
- Admin panel
- View users count
- View users list
- Broadcast message to all users

### Settings
- Language selection
- Future AI settings
- Future subscription settings

## Database Tables

### users
- id
- first_name
- username
- ai_mode
- ai_messages_count
- language

### messages
- id
- user_id
- role
- text
- created_at

## Project Status

Current version: v0.1.0

Completed:
- project structure
- config
- database
- user registration
- AI mode
- profile
- help
- settings
- admin panel
- broadcast
- logging

Next:
- refactor template
- OpenAI integration
- subscription system
- GitHub publication