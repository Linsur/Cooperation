//written by <Linsur>

package main

import (
	"fmt"

	"github.com/crawlab-team/crawlab-go-sdk/entity"
	"github.com/gocolly/colly/v2"
)

func main() {
	c := colly.NewCollector(
		colly.AllowedDomains("www.baidu.com"),
		colly.Async(true),
		colly.UserAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"),
	)

	c.OnHTML(".result.c-container", func(e *colly.HTMLElement) {
		item := entity.Item{
			"title": e.ChildText("h3.t > a"),
			"url":   e.ChildAttr("h3.t > a", "href"),
		}

		fmt.Printf("Title: %s, URL: %s\n", item["title"], item["url"])

	})

	c.OnHTML("a.n", func(e *colly.HTMLElement) {
		_ = c.Visit("https://www.baidu.com" + e.Attr("href"))
	})

	startUrl := "https://www.baidu.com/s?wd=ViterbiAlssgorithm"
	_ = c.Visit(startUrl)

	c.Wait()
}
