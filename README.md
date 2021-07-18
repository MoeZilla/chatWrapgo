# chatWrapgo

Unofficial Chatbot API wrapper for GoLang.

## Chatbot Setup 

```go

package setup

import (
	"github.com/ItelAi/chatWrapgo"
	"Setup"
)

func TestChat(t *testing.T) {
	chat, err := chatbot("hi", "misty", "moezilla", "1")
	if err != nil {
		t.Error(err)
	}
}

```


