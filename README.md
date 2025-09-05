# 🤖 Instagram Comment Bot

An advanced Instagram automation tool that intelligently comments on first posts in your timeline feed. Built with sophisticated anti-detection mechanisms to minimize the risk of account restrictions.

## ⚠️ Important Disclaimer

**This software is for educational and research purposes only.** Instagram's Terms of Service explicitly prohibit automated activities. Using this bot may result in account suspension, shadowbanning, or permanent bans. The developers assume no responsibility for any consequences arising from the use of this software. Use at your own risk.

## 🎯 Core Features

### 🕵️ Stealth Technology

- **Anti-Detection Algorithms**: Advanced timing patterns that mimic human behavior
- **Random Delay Systems**: Variable 2-8 second intervals between actions
- **API Method Fallbacks**: Automatic detection and switching between available Instagram API methods
- **Error Recovery**: Intelligent retry mechanisms with exponential backoff

### 🎨 Smart Commenting

- **First Comment Strategy**: Only targets posts with zero existing comments
- **Multi-Comment Support**: Randomly selects from your predefined comment list
- **Duplicate Prevention**: Tracks commented posts to avoid repetition
- **Age Filtering**: Skips posts older than 60 seconds for optimal engagement

### 🔧 Technical Excellence

- **Modern API Integration**: Uses `instagram-private-api` for reliable communication
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux
- **Virtual Environment Support**: Isolated dependency management
- **Comprehensive Logging**: Detailed activity tracking and error reporting

## 📋 System Requirements

- **Python**: 3.8+ (tested with Python 3.12)
- **Operating System**: Windows, macOS, or Linux
- **Instagram Account**: Active account with normal usage history
- **Internet Connection**: Stable broadband connection recommended

## 🚀 Quick Start Guide

### 1. Clone and Setup

```bash
git clone https://github.com/yourusername/instagram-commentbot.git
cd instagram-commentbot
```

### 2. Environment Setup

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install instagram-private-api colorama
```

### 4. Run the Bot

```bash
# Recommended: Stealth mode with anti-detection
python main_stealth.py

# Alternative: Standard mode
python main_modern.py
```

## 🎮 Usage Instructions

### Initial Setup

1. **Launch the bot** using one of the commands above
2. **Enter your Instagram credentials** when prompted
3. **Configure your comments** - separate multiple comments with colons:
   ```
   Great post!:Amazing content:Love this!
   ```
4. **Set refresh interval** - recommended 5-15 seconds for safety

### Bot Operation

- The bot automatically scans your timeline feed
- Identifies posts with no existing comments
- Posts random comments from your list
- Logs all activity to prevent duplicates
- Displays real-time status updates with color-coded indicators

### Status Indicators

- 🟢 **[Success]**: Comment posted successfully
- 🔵 **[Run]**: Currently posting comment
- 🟡 **[-Failed-]**: Post already has comments
- ⚪ **[Expired]**: Post is too old (>60 seconds)
- 🔴 **[-FAILED-]**: Error occurred (action blocked, etc.)

## 📁 Project Structure

```
instagram-commentbot/
├── main_stealth.py         # 🕵️ Stealth mode (RECOMMENDED)
├── main_modern.py          # 🔧 Standard mode
├── logData.txt             # 📊 Activity log (auto-generated)
├── pyproject.toml          # ⚙️ Project configuration
├── poetry.lock             # 🔒 Dependency lock file
├── venv/                   # 🐍 Virtual environment
└── README.md               # 📖 This documentation
```

## 🛡️ Anti-Detection Strategies

### Behavioral Mimicry

- **Human-like Timing**: Random delays between 2-8 seconds
- **Variable Patterns**: No fixed intervals or predictable behavior
- **Error Handling**: Longer delays on failures to avoid suspicion
- **Activity Mixing**: Designed to work alongside normal Instagram usage

### Technical Safeguards

- **API Method Detection**: Automatically finds working Instagram API endpoints
- **Session Management**: Proper handling of authentication tokens
- **Request Throttling**: Built-in rate limiting to prevent API abuse
- **Error Recovery**: Graceful handling of network and API errors

## ⚙️ Configuration Options

### Comment Management

- **Multiple Comments**: Use colons to separate different comment options
- **Random Selection**: Bot randomly chooses from your comment list
- **Customization**: Easily modify comment lists in the code

### Timing Controls

- **Refresh Intervals**: Adjustable delay between feed scans
- **Comment Delays**: Built-in random delays for human-like behavior
- **Error Recovery**: Automatic retry with exponential backoff

### Logging and Tracking

- **Activity Logs**: All commented posts saved to `logData.txt`
- **Duplicate Prevention**: Automatic tracking to avoid re-commenting
- **Status Monitoring**: Real-time feedback on bot operations

## 🚨 Troubleshooting Guide

### Common Issues and Solutions

#### Authentication Problems

```
Error: "checkpoint_challenge_required"
```

**Solution**: Complete Instagram's security challenge in your browser or mobile app, then wait 10-15 minutes before retrying.

#### API Method Errors

```
Error: "'Client' object has no attribute 'timeline_feed'"
```

**Solution**: Use `main_stealth.py` which automatically detects available API methods.

#### Python Compatibility Issues

```
Error: "ModuleNotFoundError: No module named 'cgi'"
```

**Solution**: Use Python 3.8-3.12 or ensure you're using the virtual environment.

#### Detection Warnings

```
Error: "Automated activity detected"
```

**Solution**:

- Use longer delays (10+ seconds)
- Switch to a different account
- Take breaks between sessions
- Use established accounts with normal activity history

### Best Practices for Avoidance

1. **Account Selection**

   - Use accounts 6+ months old
   - Ensure normal activity history
   - Avoid new or suspicious accounts

2. **Usage Patterns**

   - Start with minimal activity
   - Gradually increase usage over time
   - Take regular breaks (don't run 24/7)
   - Mix with normal Instagram usage

3. **Technical Considerations**
   - Use residential IP addresses
   - Avoid VPNs or datacenter IPs
   - Vary your comment content
   - Monitor for detection warnings

## 🔧 Advanced Configuration

### Customizing Comments

Edit the comment input section or modify the `commentList` variable in the code to customize your comment options.

### Adjusting Timing

Modify delay values in the code or use the interactive prompts to adjust timing parameters.

### API Endpoints

The stealth version automatically detects available Instagram API methods, but you can manually specify endpoints if needed.

## 📊 How It Works

### Technical Flow

1. **Authentication**: Establishes secure connection with Instagram
2. **Feed Retrieval**: Fetches timeline posts using Instagram's private API
3. **Content Analysis**: Filters posts based on comment count and age
4. **Comment Execution**: Posts random comments with human-like delays
5. **Activity Logging**: Records all actions to prevent duplicates
6. **Cycle Management**: Waits specified interval before next scan

### Safety Mechanisms

- **Age Filtering**: Only comments on fresh posts (<60 seconds)
- **Duplicate Prevention**: Tracks all commented posts
- **Error Handling**: Graceful recovery from API errors
- **Rate Limiting**: Built-in delays to prevent abuse

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest

# Format code
black *.py
```

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## ⚖️ Legal Notice

- **Educational Purpose**: This software is intended for educational and research purposes only
- **Terms of Service**: Users must comply with Instagram's Terms of Service
- **No Warranty**: Software provided "as is" without any warranties
- **User Responsibility**: Users assume all risks and consequences
- **No Liability**: Developers are not liable for any account actions or bans

## 🆘 Support and Community

### Getting Help

1. **Check Documentation**: Review this README thoroughly
2. **Search Issues**: Look through existing [GitHub Issues](https://github.com/yourusername/instagram-commentbot/issues)
3. **Create Issue**: Submit detailed bug reports or feature requests
4. **Community**: Join discussions in the [Discussions](https://github.com/yourusername/instagram-commentbot/discussions) section

### Contact Information

- **GitHub**: [@yourusername](https://github.com/yourusername)
- **Instagram**: [@simpifies](https://instagram.com/simpifies)

## 📈 Version History

- **v2.0.0**: Complete rewrite with stealth technology and anti-detection
- **v1.3.0**: Enhanced error handling and API compatibility
- **v1.2.0**: Multiple authentication methods and session management
- **v1.1.0**: Added stealth mode and anti-detection features
- **v1.0.0**: Initial release with basic commenting functionality

## 🔮 Future Roadmap

- [ ] Browser automation integration
- [ ] Proxy rotation support
- [ ] Advanced analytics dashboard
- [ ] Machine learning-based detection avoidance
- [ ] Multi-account management
- [ ] Scheduled posting capabilities

---

**Remember**: Use this tool responsibly and in accordance with Instagram's Terms of Service. The goal is to enhance your Instagram experience while maintaining account safety. Happy commenting! 🎉

_Last updated: January 2025_
