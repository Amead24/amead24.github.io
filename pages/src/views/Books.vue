<template>
  <v-container>
    <v-row>
      <v-col>
        <h2 class="text-center">Book Reviews</h2>
        <v-list>
          <v-list-item v-for="book in $options.books" :key="book.title">
            <v-card min-width="100%" class="my-10">
              <v-row>
                <v-col>
                  <v-card-title>{{ book.title }}</v-card-title>
                  <v-card-subtitle>{{ book.subtitle }}</v-card-subtitle>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="2">
                  <v-img
                    class="ma-5"
                    width="100%"
                    lazy-src="https://images-production.bookshop.org/spree/images/attachments/6272375/original/9780375756788.jpg?1588469852"
                  ></v-img>
                </v-col>
                <v-col cols="10">
                  <v-card-text>{{ book.content }}</v-card-text>
                </v-col>
              </v-row>
            </v-card>
          </v-list-item>
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import books_json from "/public/book_reviews.json";
// :src="require('/public/' + book.thumbnail + '_thumbnail.jpeg')"

export default {
  name: "Books",
  books: books_json,
};
</script>