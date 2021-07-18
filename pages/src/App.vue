<template>
  <v-app>
    <v-navigation-drawer
      color="red"
      v-model="drawer"
      :mini-variant.sync="mini"
      permanent
      app
    >
      <v-list-item class="px-2">
        <v-list-item-avatar>
          <v-img src="./assets/black_mage.jpeg"></v-img>
        </v-list-item-avatar>

        <v-list-item-title>Tony Mead</v-list-item-title>

        <v-btn icon @click.stop="mini = !mini">
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-item v-for="item in items" :key="item.title" :to="item.href">
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- Neeed to load conteent only in here -->
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      drawer: true,
      items: [
        { title: "Home", icon: "mdi-home-city", href: "/" },
        { title: "Resume", icon: "mdi-home-city", href: "/resume" },
        { title: "Books", icon: "mdi-home-city", href: "/books" },
      ],
      mini: true,
    };
  },
};
</script>
